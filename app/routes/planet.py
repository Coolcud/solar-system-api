from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

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

    return make_response(jsonify(f"Planet '{new_planet.planet_name}' successfully created!"), 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planet_query = request.args.get("planet_name")

    all_planets = Planet.query.all() if not planet_query else Planet.query.filter_by(planet_name=planet_query)

    # if planet_query is None:
    #     all_planets = Planet.query.all()
    # else:
    #     all_planets = Planet.query.filter_by(planet_name=planet_query)

    response = []
    for planet in all_planets:
        response.append(planet.to_dict())

    return jsonify(response), 200

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.to_dict(), 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message:": f"Planet ID '{planet_id}' is invalid."}, 400))

    return Planet.query.get_or_404(planet_id, f"Planet ID '{planet_id}' not found.")

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()
    planet.name = request_body["planet_name"]
    planet.description = request_body["description"]
    planet.num_moons = request_body["num_moons"]

    db.session.commit()

    return make_response(jsonify(f"Planet ID '{planet_id}' has been updated."), 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet ID '{planet_id}' has been deleted."), 200)