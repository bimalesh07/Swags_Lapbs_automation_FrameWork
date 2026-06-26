import pytest
from Utilities.CustomLogger import LogGen
from Utilities.ReadEnv import ReadEnvvalue

class TestBookingAPIWorkflow:
    logger = LogGen.loggen()

    #TEST 1: LOGIN 
    def test_001_logincheck(self, booking_client):
        response = booking_client.generate_token_direct(username="admin", password="password123")
        response_data = response.json()
        assert response.status_code in [200, 201]
        assert "token" in response_data

        pytest.received_token = response_data["token"]
        self.logger.info("************* Login Successful! Token Stored ************")


    # TEST 2: CREATE BOOKING
    def test_002_creating_booking(self, booking_client):
        payload = {
            "firstname": "bimalesh",
            "lastname": "yadav",
            "totalprice": 200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-07-01",
                "checkout": "2026-07-10"
            },
            "additionalneeds": "Breakfast"
        }
        response = booking_client.create_booking(payload)
        response_data = response.json()

        assert response.status_code == 200
        assert "bookingid" in response_data

        # Dynamic variable mein ID save ho gayi
        pytest.shared_booking_id = response_data["bookingid"]
        self.logger.info(f"Booking Created ID saved in pytest: {pytest.shared_booking_id}")
    

    # TEST 3: UPDATE BOOKING 
    def test_003_update_booking_secure(self, booking_client):
        booking_id = pytest.shared_booking_id
        token_value = pytest.received_token  

        update_payload = {
            "firstname": "Bimalsh",
            "lastname": "Yadav Pro QA",
            "totalprice": 300,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-07-01",
                "checkout": "2026-07-10"
            },
            "additionalneeds": "Dinner"
        }
        response = booking_client.update_booking(booking_id, update_payload, token=token_value)
        response_data = response.json()
        
        assert response.status_code in [200, 201]
        assert response_data["lastname"] == "Yadav Pro QA"
        self.logger.info(f"Booking Updated Successfully using extracted token for id: {booking_id}")
    

    # TEST 4: DELETE BOOKING 
    def test_004_delete_booking_secure(self, booking_client):
        booking_id = pytest.shared_booking_id
        token_value = pytest.received_token
        
        response = booking_client.delete_booking(booking_id, token=token_value)

        #FIX: 'assert' lagana bhool gaye the yahan, ab laga diya hai
        assert response.status_code in [200, 201, 202]
        self.logger.info(f"Booking Deleted Successfully for Id: {booking_id}")