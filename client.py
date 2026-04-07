import httpx

def login(username,password):
    with httpx.Client(base_url="https://hehenya.dpdns.org:8505") as client:
        headers = {"Content-Type":"application/json"}
        json_data = {
            "username":username,
            "password":password
        }
        response_login = client.post('/login',json=json_data)
        return response_login.json()
        