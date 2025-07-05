from flask import Flask, request, jsonify
from agent import query_ollama

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    query = data.get("query", "")
    response = query_ollama(query)
    return jsonify({'answer': str(response)})

if __name__ == "__main__":
    app.run(debug=True)