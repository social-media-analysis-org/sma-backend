from flask import Blueprint, request, jsonify
import os
from dotenv import load_dotenv
import logging
from database import collection, vector_collection
from helper import array_to_csv, upload_csv_file, get_message
from api_langflow import add_data_in_rag, query_engagement

load_dotenv()

logger = logging.getLogger(__name__)

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    skip = request.args.get('skip', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)

    match = {'rag': 'true'}

    if skip < 0 or limit < 1:
        return jsonify({"error": "Skip and Limit must be positive integers"}), 400

    data = list(collection.find(
        match,
        sort={'timestamp': 1},
        skip=skip,
        limit=limit
    ))

    data_count = collection.count_documents(match, upper_bound=1000)

    return { 'posts': data, 'posts_count': data_count }

@posts_bp.route('/posts/<post_id>', methods=['GET'])
def get_post_by_id(post_id):
    data = collection.find_one({
        '_id': post_id,
        'rag': 'true'
    })

    return {'post_details': data}

@posts_bp.route('/posts', methods=['POST'])
def add_post():
    limit = 5
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    post_type = data.get('post_type')
    post_count = data.get('post_count')

    if post_count > limit:
        return jsonify({"error": "Maximum 5 Posts can be added"}), 400

    pending_posts_match = {
        'rag': 'false',
        'type': post_type
    }
    limit = post_count
    file_name = 'social_instagram.csv'

    pending_posts = list(collection.find(
        pending_posts_match,
        limit=limit
    ))

    if len(pending_posts) < limit:
        return jsonify({"error": "Posts are not Available to be added"}), 400

    for post in pending_posts:
        collection.update_one(
            {'_id': post.get('_id')},
            {
                '$set': {
                    'rag': 'true',
                }
            }
        )

    match = {'rag': 'true'}

    data = list(collection.find(
        match
    ))

    array_to_csv(data, file_name)
    upload_csv_file(file_name)

    vector_collection.delete_all()

    file_url = os.getenv('OBJECT_URL')
    add_data_in_rag(file_url)
    os.remove(file_name)

    return {'success': True, 'message': 'Posts Added Successfully'}

@posts_bp.route('/average-engagement', methods=['GET'])
def post_type_average_engagement():
    type = request.args.get('type', default='Image', type=str)

    result = query_engagement(type)
    message = get_message(result)

    return {'result': message}
