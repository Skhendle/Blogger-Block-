from . import client
import json

# Testing the main page
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "The Entire Application"}


# Testing if new users with valid 
# credentials can register successfully.
def test_user_registration_pass1():
      
    response = client.post(
        "/user/register",
        json={
            "username": "Peter",
            "password": "string",
            "age": 20,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "message": "Successful user registration"}
    

    response = client.post(
        "/user/register",
        json={
            "username": "John",
            "password": "string",
            "age": 20,
            "gender": "male"
        }
    )
    
    assert response.status_code == 200
    assert response.json() == {"user_id": 2, "message": "Successful user registration"}
    

    response = client.post(
        "/user/register",
        json={
            "username": "Antony",
            "password": "string",
            "age": 25,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"user_id": 3, "message": "Successful user registration"}
    

# Testing user regitration with invalid details
def test_user_registration_fail():

    # Registering with unique constraint, that's already in use.
    response = client.post(
        "/user/register",
        json={
            "username": "Peter",
            "password": "pass123",
            "age": 15,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Invalid user registration"}

    # Registering with invalid input paramaters