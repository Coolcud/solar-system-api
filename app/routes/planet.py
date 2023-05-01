from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planet", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        planet_name = request_body["planet_name"],
        description = request_body["description"],
        num_moons = request_body["num_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet '{new_planet.planet_name}' successfully created!"), 201

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        response.append(planet.to_dict())

    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"message:": f"Planet ID '{planet_id}' is invalid."}), 400

    all_planets = Planet.query.all()
    for planet in all_planets:
        if planet.id == planet_id:
            return planet.to_dict(), 200

    return jsonify({"message": f"Planet '{planet_id}' does not exist."}), 404