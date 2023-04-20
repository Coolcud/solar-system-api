from flask import Blueprint, jsonify

class Planet: 
    def __init__(self, id, planet_name, number_of_moons, distance_from_sun):
        self.id = id
        self.planet_name = planet_name
        self.number_of_moons = number_of_moons
        self.distance_from_sun = distance_from_sun
planets_list = [
    Planet(1, "Mercury", 0, "36.43 million mi"),
    Planet(2, "Venus", 0, "66.79 million mi"),
    Planet(3, "Earth", 1, "93.39 million mi"),
    Planet(4, "Mars", 2, "155.04 million mi"),
    Planet(5, "Jupiter", 90, "460.43 million mi"),
    Planet(6, "Saturn", 83, "910.54 million mi"),
    Planet(7, "Uranus", 27, "1.83 billion mi"),
    Planet(8, "Neptune", 14, "2.78 billion mi")
]

planets_bp = Blueprint("planet", __name__, url_prefix="/planets") 

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets_list:
        response.append({
            "id": planet.id,
            "planet_name": planet.planet_name,
            "number_of_moons": planet.number_of_moons,
            "distance_from_sun": planet.distance_from_sun 
        })
    return jsonify(response), 200