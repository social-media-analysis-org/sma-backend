from flask import Blueprint, request, jsonify
import logging
from dotenv import load_dotenv
from api_langflow import fetch_result
from helper import get_message

load_dotenv()

logger = logging.getLogger(__name__)

chats_bp = Blueprint('chat', __name__)

@chats_bp.route('/chat', methods=['GET'])
def process_query():
    query = request.args.get('query', type=str)

    if query is None:
        return jsonify({"error": "No JSON data provided"}), 400

    result = fetch_result(query)
    message = get_message(result)

    return {"message": message}
