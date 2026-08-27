import pytest
from api.posts import PostsApi
from config.config import base_url
from common.request import Request
from config.config import timeout

@pytest.fixture
def posts_api(request_client):
    return PostsApi(base_url,request_client)

@pytest.fixture
def request_client():
    return Request(timeout=timeout)

@pytest.fixture
def http_request(request):
    http_request=Request(timeout=timeout)
    yield http_request
    if http_request.last_request:
        request.node.user_properties.append(
            ("请求URL",http_request.last_request["url"]
            )
        )

def pytest_configure(config):
    from pytest_metadata.plugin import metadata_key
    config.stash[metadata_key] ["项目"]= "API自动化测试项目"
    config.stash[metadata_key]["测试环境"]="test"