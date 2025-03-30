import requests

def make_api_call(content):
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "web_access": False
    }
    headers = {
        "content-type": "application/json",  # Sending JSON data
        "Accept": "text/plain",  # Expecting plain text (JavaScript) in response
        "X-RapidAPI-Key": "8e78024b1cmsh6b6c6140597751fp18d9e3jsn81dc3f112100",
        "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.text  # Get response as plain text

# # Example usage
# output = make_api_call("Generate JavaScript code")
# print(output)
