from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"status":"successful", "info" :"Hello, this is the root URL!"})

@app.route('/get')
def get_data():
    return jsonify({"data": {"item1":"value 1", "item2":"value2"}})


if __name__ == '__main__':
    app.run(debug=True)
    