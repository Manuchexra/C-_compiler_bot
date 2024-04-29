import requests
from tinydb import TinyDB, Query
from config import clientId, clientSecret

db = TinyDB("db.json", indent=4)
item = Query()
users_table = db.table("users")

def compile_cpp_code(code: str, userid) -> str:
    url = "https://api.jdoodle.com/v1/execute"
    user = db.table("users").get(item.user_id==userid)
    tests = db.table("tasks").get(doc_id=user["completed_tasks"]+1)["test"]
    accept = 0
    for i in range(0,5):
        input_data = tests["input"][i]
        payload = {
            "clientId": clientId,
            "clientSecret": clientSecret,
            "script": code,
            "language": "cpp",
            "versionIndex": "0",
            "stdin":input_data
        }
        response = requests.post(url, json=payload)
        if str(response.json()["output"])==tests["output"][i]:
            accept+=1
    if accept==5:
        number = user["completed_tasks"]+1
        users_table.update({"completed_tasks":number}, item.user_id==userid)
        return "Ajoyib! Siz buni uddaladingiz!"
    else:
        return "Afsus kodingizda xatolik borga o'xshaydi, yana bir bor urunib ko'ring"

def task(userid):
    user = db.table("users").get(item.user_id==userid)
    task = db.table("tasks").get(doc_id=(int(user["completed_tasks"])+1))
    text = f"""{task["name"]}

{task["question"]}
"""
    return text

def task_titles():
    tasks = db.table("tasks")
    print()

def add_user(user_name, user_id):
    if not users_table.get(item.user_id==user_id):
        new_user = {
            'name': user_name,
            'user_id': user_id,
            'completed_tasks': 0
        }

        users_table.insert(new_user)
    
    

