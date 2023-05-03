import pytest

def test_get_one_planet_with_no_data(client):
    response = client.get("/planets/1")

    response_body = response.get_json()

    assert response.status_code == 404

def test_get_one_planet(client, two_planets):
    response = client.get("/planets/1")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "planet_name": "Uranus",
        "description": "A baby blue ice giant",
        "num_moons": 27
    }

def test_get_all_planets(client, two_planets):
    response = client.get("/planets")

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "planet_name": "Uranus",
        "description": "A baby blue ice giant",
        "num_moons": 27
    },
    {
        "id": 2,
        "planet_name": "Mars",
        "description": "A reddish, dusty, cold desert",
        "num_moons": 2
    }]

def test_post_creates_planet(client):
    response = client.post("/planets", json= {
        "planet_name": "Uranus",
        "description": "A baby blue ice giant",
        "num_moons": 27
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet 'Uranus' successfully created!"
