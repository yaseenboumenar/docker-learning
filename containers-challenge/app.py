
import os
import redis
from flask import Flask, jsonify

r = redis.Redis(
    host=os.environ.get("MYREDIS_HOST", "redis"),
    port=int(os.environ.get("MYREDIS_PORT", 6379)),
    db=0
)

app = Flask(__name__)           # Instance of our flask web app

@app.route('/')
def home():
    return "Welcome to the challenge!"

# @app.route('/count')
# def get_count():
#     count = r.incr("visits")
#     return jsonify({"visit_count": count})


@app.route('/count')
def get_count():
    try:
        count = r.incr("visits")
        return jsonify({"visit_count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':                  # Configured to run on all IP addresses
    app.run(host='0.0.0.0', port=80)
