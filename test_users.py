import requests

response = requests.post("http://127.0.0.1:8080/api/v2/users",
                         json={
    "surname": "abc",
    "name": "daf",
    "age": 20,
    "position": "deployment of residential modules 1 and 2 and 3",
    "speciality": "None",
    "address": "hello",
    "email": "some@thing.com",
    "modified_date": None,
    "hashed_password": "not_so_hashed"
                         })
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.delete("http://127.0.0.1:8080/api/v2/users/6")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.get("http://127.0.0.1:8080/api/v2/users/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.get("http://127.0.0.1:8080/api/v2/users/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")
