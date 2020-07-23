from flask import current_app as app
from flask import request, make_response
from os import sys
from src.models.planet import Planet
from mongoengine import ValidationError

@app.route('/planet', methods=['POST'])
def add_planet():

    planet_data = request.get_json()

    name = planet_data.get("name")
    orbital_speed = planet_data.get('orbital_speed')
    circumference = planet_data.get('circumference')

    response = make_response('', 505)

    try:
        planet = Planet(name=name, orbital_speed=orbital_speed, circumference=circumference)
        planet.save()
        response = make_response(f'Planet {name} successfuly added!', 200)
        
    except ValidationError as error :
        response = make_response(f'Planet doesn\'t have a name, it couldn\'t be added ({error})!', 505)
    except Exception as error :
        response = make_response(f'Planet {name} couldn\'t be added because {error}!', 505)
    
    return response