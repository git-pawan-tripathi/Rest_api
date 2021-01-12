import requests
import json

URL=" http://127.0.0.1:8000/stu/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    print(r.json())

#get_data(2)
def create_stu():
    data={
    'name':'chetan',
    'roll':1004,
    'city':'kalapani'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    print(r.json())

#create_stu()
def update_stu():
    data={'id':'5','name':'ketan'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    print(r.json())

#update_stu()
def delete_stu():
    data={'id':2}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    print(r.json())

delete_stu()