from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for blog posts
posts = []

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/api/posts', methods=['POST'])
def create_post():
    post_data = request.get_json()
    posts.append(post_data)
    return jsonify(post_data), 201

if __name__ == '__main__':
    app.run(debug=True)
