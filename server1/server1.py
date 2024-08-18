from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def handle_message():
    # Get the JSON data from the request
    data = request.json
    
    # Extract the message from the JSON data
    message = data.get('message', '')
    
    # Log the received message (optional)
    print(f"Received message: {message}")
    
    # Respond with "Hi"
    response = {"response": "Hi"}
    
    return jsonify(response), 200

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000)
