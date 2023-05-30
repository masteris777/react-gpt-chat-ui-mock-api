from flask import Flask, request, jsonify
from flask_cors import CORS
from base64 import b64encode
import asyncio
import os

app = Flask(__name__)
CORS(app) # Add CORS middleware

def convert_to_base64_chunk(str):
    return f"{b64encode(str.encode()).decode()}\n"

@app.route('/api/models', methods=['GET'])
async def get_models():
    print("got models request")
    return jsonify({
        'models': [
            {
                'name': "GPT-1",
            },
            {
                'name': "GPT-2",
            },
            {
                'name': "GPT-3",
            },
        ]
    })

@app.route('/api/summaries', methods=['POST'])
async def post_summaries():
    print("got summary request")
    messages = request.json.get('messages')
    if not messages or not messages[0]:
        print("no messages")
        return jsonify({"error": "Message is required"}), 400

    return jsonify({'summary': messages[0]['text'][:20]})

@app.route('/api/models/<model>/conversations', methods=['POST'])
async def post_conversations(model):
    print("got conversations request")
    messages = request.json.get('messages')
    if not messages or not messages[0]:
        print("no messages")
        return jsonify({"error": "Message is required"}), 400

    file = f"./stories/story{len(messages[-1]['text']) % 4}.md"
    with open(file, 'r') as f:
        story = f.read()
    words = story.split(" ")

    @app.after_request
    def after_request(response):
        print("end")
        return response

    def generate():
        for word in words:
            yield convert_to_base64_chunk(word + " ")
            asyncio.sleep(0.1)

    return app.response_class(generate(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(port=3001)
