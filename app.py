from flask import Flask, jsonify, request

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask Server!"

# Sample route to return JSON data
@app.route('/data', methods=['GET'])
def get_data():
    sample_data = {"message": "Hello, this is sample data from the server!"}
    return jsonify(sample_data)

# Sample route to handle POST requests
@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
