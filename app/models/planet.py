from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    planet_name = db.Column(db.String)
    description = db.Column(db.String)
    num_moons = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "description": self.description,
            "num_moons": self.num_moons
        }