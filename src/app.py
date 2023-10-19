from flask import Flask, jsonify, request

from .model import is_query_valid, load_model, sample

model = load_model()

app = Flask(__name__)


@app.route("/")
def hello_world():
    q = request.args.get("q", "a")

    if not is_query_valid(q):
        return jsonify({"error": f"Invalid query"}), 400

    prediction = sample(model, q)

    return jsonify({"prediction": prediction})
