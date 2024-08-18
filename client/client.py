import requests
import json

# Define the server URL
SERVER_URL = "http://localhost:5000/message"  # Replace with your server URL if different

def send_message():
    # The message to be sent
    message = {"message": "Hello"}
    
    try:
        # Send a POST request to the server with the message
        response = requests.post(SERVER_URL, json=message)
        
        # Print the response from the server
        if response.status_code == 200:
            print("Server Response:", response.json())
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_message()
