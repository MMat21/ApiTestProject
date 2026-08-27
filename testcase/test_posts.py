import pytest
from common.read_data import read_json,read_update_data
from config.config import base_url
from api.posts import PostsApi

def test_get(posts_api):
   result=posts_api.get_todo()
   print(result)
   assert result["status_code"]==200
   assert result["data"]["id"]==1

@pytest.mark.parametrize(
    "data",
    read_json()
)
def test_post(data,posts_api):
    result=posts_api.create_post(data)
    print(result)
    assert result["status_code"]==201
    assert result["data"]["id"]==data["expected_id"]
    assert result["data"]["title"]==data["title"]
    assert result["data"]["body"]==data["body"]

@pytest.mark.parametrize(
    "data",
    read_update_data()
)
def test_update(data,posts_api):
    result=posts_api.update_post(1,data)
    print(result)
    assert result["status_code"]==200
    assert result["data"]["id"]==1
    assert result["data"]["title"]==data["title"]
    assert result["data"]["body"]==data["body"]
    assert result["data"]["userId"]==data["userId"]

def test_delete(posts_api):
    result=posts_api.delete_post(1)
    print(result)
    assert result["status_code"]==200

def test_get_post(posts_api):
    result=posts_api.get_post(1)
    print(result)
    assert result["status_code"]==200
    assert result["data"]["id"]==1

def test_get_post_not_found(posts_api):
    result=posts_api.get_post(9999)
    print(result)
    assert result["status_code"]==404

@pytest.mark.parametrize("post_id", [0, -1, 9999])
def test_get_post_invalid_id(posts_api, post_id):
    result = posts_api.get_post(post_id)
    print(result)
    assert result["status_code"]==404
