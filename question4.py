import requests
import json

def send_json_payload(data):
    url = "https://api.example.com/submit"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(data)
    
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        print("Request successful.")
        print("Response:", response.text)
    else:
        print("Request failed. Status code:", response.status_code)


# Example data to send as JSON payload
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com"
}

# Call the function with the example data
send_json_payload(data)
