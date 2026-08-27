import requests
from common.logger import logger
class Request:
    def __init__(self,timeout=10):
        self.headers = {}
        self.timeout = timeout
        self.last_request={}

    def set_headers(self,headers):
        self.headers.update(headers)

    def _update_headers(self,headers):
        if headers :
            self.headers.update(headers)

    def _send_request(self,method,url,**kwargs):
        self.last_request={
            "method":method,
            "url":url,
            "kwargs":kwargs
        }
        logger.info("请求方法:%s", method)
        logger.info("请求URL:%s", url)
        logger.info("请求参数:%s", kwargs)
        try:
            response = requests.request(method=method,url=url,**kwargs)
            return response
        except requests.exceptions.Timeout:
            logger.error("请求超时:%s",url)
            raise
        except requests.exceptions.ConnectionError:
            logger.error("连接失败:%s",url)
            raise

    def get(self, url, params=None, headers=None, timeout=None):
        if timeout is None:
            timeout = self.timeout
        logger.info("发送GET请求:%s", url)
        self._update_headers(headers)
        response = self._send_request(
            method="GET",
            url=url,
            params=params,
            headers=self.headers,
            timeout=timeout
        )
        return self._handle_response(response)
       # response=requests.get(url,params=params,headers=self.headers,timeout=timeout)
       # return self._handle_response(response)

    def post(self, url, data=None, headers=None, timeout=None):
        if timeout is None:
            timeout = self.timeout
        logger.info("发送POST请求:%s", url)
        self._update_headers(headers)
        response = self._send_request(
            method="POST",
            url=url,
            json=data,
            headers=self.headers,
            timeout=timeout
        )
        return self._handle_response(response)
       # response=requests.post(url=url ,json=data,headers=self.headers, timeout=timeout)
       # return self._handle_response(response)

    def put(self, url, data=None, headers=None, timeout=None):
        if timeout is None:
            timeout = self.timeout
        logger.info("发送PUT请求:%s", url)
        self._update_headers(headers)
        response = self._send_request(
            method="PUT",
            url=url,
            json=data,
            headers=self.headers,
            timeout=timeout
        )
        return self._handle_response(response)
       # response = requests.put(url=url,data=data,headers=self.headers,timeout=timeout)
       # return self._handle_response(response)

    def delete(self, url, params=None, headers=None, timeout=None):
        if timeout is None:
            timeout = self.timeout
        logger.info("发送DELETE请求:%s", url)
        self._update_headers(headers)
        response = self._send_request(
            method="DELETE",
            url=url,
            params=params,
            headers=self.headers,
            timeout=timeout
        )
        return self._handle_response(response)
       # response = requests.delete(url=url,params=params,headers=self.headers,timeout=timeout)
       # return self._handle_response(response)

    def _handle_response(self,response):
        logger.info("状态码:%s", response.status_code)
        logger.info("返回内容:%s", response.text)
        try:
            data=response.json()
        except requests.exceptions.JSONDecodeError:
            data=response.text
        return {
            "status_code":response.status_code,
            "data":data
        }
