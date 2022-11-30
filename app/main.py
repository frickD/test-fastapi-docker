import requests
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class Notification(BaseModel):
    title: str
    msg: Union[str, None] = None

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/cn/")
async def create_notification(notification: Notification):
    return notification

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/notification/{title}")
def read_notification_item(title: str, msg: Union[str, None] = None):
    r = requests.post("http://test-fastapi-docker-git-app-node-test.openshift-cluster-df-10824457b4a919156a145e0783a45645-0000.eu-de.containers.appdomain.cloud/cn/", data={'title': title, 'msg': msg})
    print(r.status_code, r.reason)
    return r.text[:300] + '...'

