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

# 1.消息发送获取类
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

    def delete_message(self, message_id):
        url = f"{self.base_url}/delete_message"
        data = {
            "message_id": message_id,
            "status": 1  
        }
        try:
            response = httpx.post(url, headers=self.headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"


    def update_message(self, message_id, new_content=None, new_message_type=None, 
                       new_title=None, visible_to=None, is_markdown=None):
        url = f"{self.base_url}/update_message"
        data = {
            "message_id": message_id
        }
        
        if new_content is not None:
            data["new_content"] = new_content
        if new_message_type is not None:
            data["new_message_type"] = new_message_type
        if new_title is not None:
            data["new_title"] = new_title
        if visible_to is not None:
            data["visible_to"] = visible_to
        if is_markdown is not None:
            data["is_markdown"] = is_markdown
            
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
class User:
    def __init__(self, token=""):
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

    def get_all_users(self, page=1, per_page=20, search=''):
        url = f"{self.base_url}/get_all_users"
        params = {
            "page": page,
            "per_page": per_page,
            "search": search
        }
        try:
            response = httpx.get(url, headers=self.headers, params=params)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def get_user_info_by_username(self, userid):
        url = f"{self.base_url}/user_info"
        data = {
            "user_id": userid
        }
        try:
            response = httpx.post(url, headers=self.headers, json=data)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"

    def get_user_info_by_token(self):
        url = f"{self.base_url}/user_info_token"
        try:
            response = httpx.post(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"
# 3.通知获取类
class Notification:
    def __init__(self, token=""):
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

    def get_notifications(self, notification_type=None, page=1, per_page=20):
        url = f"{self.base_url}/v2/notifications"
        params = {
            "page": page,
            "per_page": min(per_page, 100)
        }
        
        if notification_type is not None:
            params["type"] = notification_type
        
        try:
            response = httpx.get(url, headers=self.headers, params=params)
            return response.json()
        except Exception as e:
            return f"请求出错: {str(e)}"