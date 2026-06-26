import pytest
import requests

#thi is main url and endpoints
BASE_URL = "https://reqres.in"
ENDPOINT = "/api/register"

def test_quick_register_user():
    #make complete url
    final_url = f"{BASE_URL}{ENDPOINT}"
    
    #3 Payload to send data 
    signup_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    
    # Common Headers for send jwt token also
    headers = {
        "Content-Type": "application/json"
    }
    
    #4. API EndPoint hit (POST Request)
    response = requests.post(final_url, json=signup_payload, headers=headers)
    
    #5.Check response validation (Assertions) kiya
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    json_data = response.json()
    assert "id" in json_data, "Response mein id missing hai"
    assert "token" in json_data, "Response mein token missing hai"
    
    # Console just to see 
    print(f"\n Quick Test Success! Token mila: {json_data['token']}")