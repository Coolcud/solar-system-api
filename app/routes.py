from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, planet_name, description, num_of_moons):
        self.id = id
        self.planet_name = planet_name
        self.description = description
        self.num_of_moons = num_of_moons

planets_list = [
    Planet(1, "Mercury", "A grey, rocky planet", 0),
    Planet(2, "Venus", "A yellow-white, marble planet", 0),
    Planet(3, "Earth", "A blue marble with different colored swirls", 1),
    Planet(4, "Mars", "A reddish, dusty, cold desert", 2),
    Planet(5, "Jupiter", "Covered in swirling cloud stripes", 90),
    Planet(6, "Saturn", "Unique planet with rings of ice", 83),
    Planet(7, "Uranus", "A baby blue ice giant", 27),
    Planet(8, "Neptune", "A dark blue planet with supersonic winds", 14)
]

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets_list:
        response.append({
            "id": planet.id,
            "planet_name": planet.planet_name,
            "description": planet.description,
            "number_of_moons": planet.num_of_moons
        })
    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"message:": f"ID '{planet_id}' is invalid."}), 400

    for planet in planets_list:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "planet_name": planet.planet_name,
                "description": planet.description,
                "number_of_moons": planet.num_of_moons
            }, 200
    return jsonify({"message": f"Planet '{planet_id}' does not exist."}), 404
