from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def handle_message():
   
    data = request.json
    
   
    message = data.get('message', '')
    
    
    print(f"Received message: {message}")
    
   
    response = {"response": "Hi"}
    
    return jsonify(response), 200

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000)
