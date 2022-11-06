from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data = {"name": "keisuke", "age": 16, "message": "Hello API"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
