import requests

response = requests.post("http://127.0.0.1:8080/api/v2/jobs",
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

response = requests.delete("http://127.0.0.1:8080/api/v2/jobs/9")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.get("http://127.0.0.1:8080/api/v2/jobs/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.get("http://127.0.0.1:8080/api/v2/jobs/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")
