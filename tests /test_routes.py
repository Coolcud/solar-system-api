import pytest

def test_get_all_planets(client, two_planets): 
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200 
    assert response_body == [{
        "planet_name": "Uranus",
        "description": "A baby blue ice giant",
        "num_moons": 27
    },
    {    
        "planet_name": "Mars",
        "description": "A reddish, dusty, cold desert",
        "num_moons": 2
    }]