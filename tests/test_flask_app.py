from api.flask_app import app
import json
from typing import List


def test_index_route():
    response = app.test_client().get("/api/text=Test")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert type(res) is dict
    assert type(res["text"][0]) is str
    assert type(res["tags"]) is list
    assert type(res["tags"][0]) is list
    assert type(res["tags"][0][0]) is str

def test_index_route_bis():
    response = app.test_client().get("/api/text=python")
    res = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert type(res) is dict
    assert type(res["text"][0]) is str
    assert type(res["tags"]) is list
    assert type(res["tags"][0]) is list
    assert type(res["tags"][0][0]) is str

