from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/stuff')
def names():
    data = {"favourites": {"films":["LOTR", "Space Jam", "Star Wars", "Krull"]}}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
