import requests
def make_api_call(content):
    url = "https://chatgpt-42.p.rapidapi.com/gpt4"
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
        "content-type": "application/json",
        "x-rapidapi-key": "your_api_key",
	    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()



# import requests
# def make_api_call(content):
#     url = "https://open-ai21.p.rapidapi.com/"
#     payload = {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ],
#         "web_access": False
#     }
#     headers = {
#         "content-type": "application/json",
#         "x-rapidapi-key": "your_api_key",
# 	     "x-rapidapi-host": "open-ai21.p.rapidapi.com"

#     }
#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()


# import requests
# def make_api_call(content):
#     url = "https://chatgpt-api8.p.rapidapi.com/gpt4"
#     payload = {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ],
#         "web_access": False
#     }
#     headers = {
#         "x-rapidapi-key": "your_api_key",
# 	    "x-rapidapi-host": "chatgpt-api8.p.rapidapi.com",
# 	    "content-type": "application/json"
# }
#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()


# import requests

# def make_api_call(query, sys_msg="You are a friendly Chatbot."):
#     url = "https://infinite-gpt.p.rapidapi.com/infinite-gpt"
    
#     payload = {
#         "query": query,
#         "sysMsg": sys_msg
#     }
    
#     headers = {
#         "x-rapidapi-key": "your_api_key",
#         "x-rapidapi-host": "infinite-gpt.p.rapidapi.com",
#         "Content-Type": "application/json"
#     }
    
#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()


# import requests

# def make_api_call(question):
#     url = "https://chat-gpt-3-5-turbo2.p.rapidapi.com/problem.json"
    
#     querystring = {"question": question}
    
#     headers = {
#         "x-rapidapi-key": "your_api_key",
#         "x-rapidapi-host": "chat-gpt-3-5-turbo2.p.rapidapi.com"
#     }
    
#     response = requests.get(url, headers=headers, params=querystring)
#     return response.json()
