import requests

class BookingEndpoints:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Content_Type": "application/json", "Accept":"application/json"}

    def  generate_token_direct(self, username, password):
        url = f"{self.base_url}/auth"
        payload = {"username":username, "password":password}
        response = requests.post(url, json=payload, headers=self.headers)
        return response
    
    #create a booking 
    def create_booking(self, booking_data):
        url = f"{self.base_url}/booking"
        response = requests.post(url, json=booking_data, headers=self.headers)
        return response
    
    def update_booking(self, booking_id, update_data, token):
        url = f"{self.base_url}/booking/{booking_id}"

        #send cookies in headers 
        headers = self.headers.copy()
        headers["Cookie"] = f"token={token}"

        response = requests.put(url, json=update_data, headers=headers)
        return response
    
    def delete_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers =  self.headers.copy()
        headers["Cookie"] = f"token={token}"
        response = requests.delete(url, headers=headers)
        return response
    
    

        
