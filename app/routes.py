from flask import Blueprint, jsonify,

class Planet:
    def __init__(self, id, planet_name, num_of_moons, description):
        self.id = id
        self.planet_name = planet_name
        self.num_of_moons = num_of_moons
        self.description = description

planets_list = [
    Planet(1, "Mercury", 0, "A grey, rocky planet"),
    Planet(2, "Venus", 0, "A yellow-white, marble planet"),
    Planet(3, "Earth", 1, "A blue marble with different colored swirls"),
    Planet(4, "Mars", 2, "A reddish, dusty, cold desert"),
    Planet(5, "Jupiter", 90, "Covered in swirling cloud stripes"),
    Planet(6, "Saturn", 83, "Unique planet with rings of ice"),
    Planet(7, "Uranus", 27, "A baby blue ice giant"),
    Planet(8, "Neptune", 14, "A dark blue planet with supersonic winds")
]

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    for planet in planets_list:
        response.append({
            "id": planet.id,
            "planet_name": planet.planet_name,
            "number_of_moons": planet.num_of_moons,
            "description": planet.description
        })
    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message:": f"ID '{planet_id}' is invalid."}, 400

    for planet in planets_list:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "planet_name": planet.planet_name,
                "number_of_moons": planet.num_of_moons,
                "description": planet.description
            }, 200

    return {"message": f"Planet '{planet_id}' does not exist."}, 404
