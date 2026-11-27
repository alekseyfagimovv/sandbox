# import requests
  

# def fetch_user_data(user_id: int) -> dict | None:
#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     headers = {"Accept": "application/json"}
#     try:
#         response = requests.get(url, timeout=3, headers=headers)
#         if response.status_code == 404:
#             return None
#         response.raise_for_status()  # выбросит HTTPError для 4xx/5xx (кроме 404)
#         return response.json()
        
#     except (requests.ConnectionError, requests.Timeout):
#         return None
        
# user = fetch_user_data(19999)
# if user:
#     print(user["name"])  # "Leanne Graham"
# else:
#     print("Пользователь не найден или ошибка сети")
# user = fetch_user_data(1)
# if user:
#     print(user["name"])  # "Leanne Graham"
# else:
#     print("Пользователь не найден или ошибка сети")
 

# def safe_get(url):
#     try:
#         response = requests.get(url, timeout=2)
#     except (requests.ConnectionError, requests.Timeout):
#         return "network_error"
#     if response.status_code == 404:
#         return "not_found"
#     if response.status_code == 500:
#         return "server_error"
#     if response.status_code == 200:
#         return response.json()
#     return "unexpected_status"

# import requests


# def check_user_creation(url, payload, token=None):
#     token = {"Authorization": f"Bearer {token}"}
#     try:
#         with requests.post(url, json=payload, headers=token, timeout=5) as r:
#             assert r.status_code == 201
#             print(r.json())
#             return r.json()["id"]
#     except (requests.ConnectionError, requests.Timeout) as e:
#         print("Ошибка сети!")
#         raise e


# result = check_user_creation(url="https://jsonplaceholder.typicode.com/todos", payload={"title": 'Мой новый пост',
#   "body": 'Текст поста', "userId": 1})
# print(result)