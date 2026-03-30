import requests

response = requests.post("http://127.0.0.1:8080/api/jobs",
                         json={
    "collaborators": "3, 4",
    "end_date": None,
    "is_finished": False,
    "job": "deployment of residential modules 1 and 2 and 3",
    "start_date": None,
    "team_leader": 1,
    "work_size": 15
                         })
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.post("http://127.0.0.1:8080/api/jobs",
                         json={
    "collaborators": "3, 4",
    "end_date": None,
    "is_finished": "hi",
    "job": "deployment of residential modules 1 and 2 and 3",
    "start_date": None,
    "team_leader": 1,
    "work_size": "15"
                         })
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.post("http://127.0.0.1:8080/api/jobs",
                         json={
    "collaborators": "3, 4",
    "end_date": None,
    "is_finished": None,
    "job": "deployment of residential modules 1 and 2 and 3",
    "start_date": None,
    "team_leader": None,
    "work_size": 15
                         })
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.post("http://127.0.0.1:8080/api/jobs",
                         json={
    "collaborators": "3, 4",
    "end_date": None,
    "is_finished": False,
    "job": "deployment of residential modules 1 and 2 and 3",
    "start_date": None,
    "team_leader": 1,
    "work_size": 15,
    "id": "yes"
                         })
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")
