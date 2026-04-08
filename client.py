import httpx
import json
def login(username,password):
    with httpx.Client(base_url="https://hehenya.dpdns.org:8505") as client:
        headers = {"Content-Type":"application/json"}
        json_data = {
            "username":username,
            "password":password
        }
        response_login = client.post('/login',json=json_data)
        return response_login.json()
        
        
# 此处来自qz_user_sdk        
class Post:
    def __init__(self,token = ""):
        self.base_url = "https://hehenya.dpdns.org:8505"
        self.token = token        
        self.headers = {
            "Accept-Language": "zh-cn,zh;q=0.5",
            "Accept-Charset": "UTF-8",
            "x-access-token": self.token,
            "Content-Type": "application/json",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }

    def send_message(self, content, category_id, message_type=None, is_markdown=None,title=None):
        url = f"{self.base_url}/post_message"
        data = {
            "category_id": category_id,
            "content": content
        }
        
        if is_markdown:
            data["is_markdown"] = is_markdown
        if message_type:
            data["message_type"] = message_type
        if title:
            data["title"] = title    
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def like_message(self, message_id):
        url = f"{self.base_url}/like_message"
        data = {"message_id": message_id}
        
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return str(e)

    def get_messages(self, category_id, page, per_page):
        url = f"{self.base_url}/v3/get_message?category_id={category_id}&page={page}&per_page={per_page}"
        
        try:
            response = httpx.get(url, headers=self.headers)
            return response.json()
        except httpx.RequestException as e:
            return f"请求出错: {str(e)}"
            
    def reply_to_message(self, content, category_id, referenced_message_id):
        url = f"{self.base_url}/post_referenced_message"
        data = {
            "content": content,
            "category_id": category_id,
            "referenced_message_id": referenced_message_id
        }
        
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
            