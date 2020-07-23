import pytest
import json
from src import create_app
from src.models.planet import Planet


@pytest.fixture
def setup_server_db():
    
    app = create_app()
    client = app.test_client()
    
    yield client
    
    Planet.drop_collection()

def test_POST_plannet(setup_server_db):
    planet  = { "name" : "Earth", "orbital_speed" : 29.78, "circumference" : 40.075 }
    resp    = setup_server_db.post("/planet", json=planet)
    assert resp.status_code == 200
    assert resp.get_data("text") == f'Planet {planet["name"]} successfuly added!'
