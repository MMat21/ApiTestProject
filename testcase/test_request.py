from config.config import httpbin_url
from common.request import Request

def test_header(http_request):
    headers = {"X-Test-Header": "hello"}

    result = http_request.get(
        httpbin_url+"/headers",
        headers=headers
    )
    print(result)
    assert result["status_code"] == 200
    assert result["data"]["headers"]["X-Test-Header"] == "hello"
   # result = http_request.get("https://httpbin.org/headers",headers=headers)
   # print(result)
   # assert result["status_code"]==200
   # assert result["data"]["headers"]["X-Test-Header"]=="hello"

def test_headers():
    request = Request()
    # 公共headers
    request.set_headers({
        "Authorization": "Bearer abc123"
    })
    # 额外增加一个headers
    result = request.get(
        httpbin_url+"/headers",
        headers={"X-Test-Header": "hello"}
    )
    print(result)
    assert result["data"]["headers"]["Authorization"] == "Bearer abc123"
    assert result["data"]["headers"]["X-Test-Header"] == "hello"
   # token="abc123"
   # request.set_headers({"Authorization":f"Bearer {token}"})
   # result=request.get("https://httpbin.org/headers")
   # print(result)
   # assert result["data"]["headers"]["Authorization"] == "Bearer abc123"
   # result2=request.get("https://httpbin.org/headers")
   # print(result2)
   # assert result2["data"]["headers"]["Authorization"] == "Bearer abc123"

def test_params(http_request):
    params={"name":"Tom","age":18}
    result = http_request.get(httpbin_url+"/get",params=params)
    print(result)
    assert result["status_code"]==200