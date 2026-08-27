from config.api import posts_url,todos_url
class PostsApi:
    def __init__(self,base_url,request):
        self.base_url=base_url
        self.request=request

    def _url(self,path):
        return self.base_url+path

    def create_post(self,data):
        return self.request.post(url=self._url(posts_url),data=data)

    def update_post(self,post_id,data):
        request_data={
            "title":data["title"],
            "body":data["body"],
            "userId":data["userId"],
        }
        return self.request.put(url=self._url(posts_url) + "/" + str(post_id),data=request_data)

    def get_todo(self):
        return self.request.get(url=self._url(todos_url))

    def get_post(self, post_id):
        return self.request.get(
            url=f"{self.base_url}{posts_url}/{post_id}"
        )

    def delete_post(self,post_id):
        return self.request.delete(
            url=self._url(posts_url) + "/" + str(post_id)
        )

