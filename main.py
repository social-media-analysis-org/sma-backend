import os
from flask import Flask, jsonify
from datetime import datetime
from routes.posts import posts_bp
from routes.chat import chats_bp
from flask_cors import CORS
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.urandom(24)

origins = os.getenv('FRONTEND_URL').split(',')

CORS(app, resources={
    r"/*": {
        "origins": os.getenv('FRONTEND_URL')
    }
})

app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(chats_bp, url_prefix='/chat')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(Exception)
def handle_error(error):
    logger.error(f'An error occurred: {str(error)}')
    return jsonify({'error': 'Internal server error'}), 500

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
