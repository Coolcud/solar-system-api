import pytest 
from app import create_app, db
from app.models.planet import Planet 
from flask.signals import request_finished

@pytest.fixture 
def app(): 
    app = create_app(testing=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app 
        db.drop_all()
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_planets():
    uranus = Planet(
        planet_name="Uranus",
        description="A baby blue ice giant",
        num_moons = 27
    )
    mars = Planet(
        planet_name="Mars",
        description="A reddish, dusty, cold desert",
        num_moons = 2
    )
    db.session.add_all([uranus, mars])
    db.session.commit()
