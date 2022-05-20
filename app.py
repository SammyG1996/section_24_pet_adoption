'''Pet Adoption Application'''

from crypt import methods
from dataclasses import dataclass
from flask import Flask, redirect, render_template
from secret import secret_key
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetFrom


# this is initiate the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = secret_key

debug = DebugToolbarExtension(app)

# this will connect the app to the DB
connect_db(app)

@app.route('/')
def homepage():
  '''This will contain all the pets that are currently posted on the application'''
  pets = Pet.query.all()
  return render_template('homepage.html', pets = pets)

@app.route('/new_pet', methods=['POST', 'GET'])
def add_new_pet():
  '''this will allow users to create a new pet'''
  form = AddPetFrom()
  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data

    db.session.add(Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available))
    db.session.commit()
    return redirect('/')
    
  else:
    return render_template('add_pet.html', form = form)

@app.route('/pet/<pet_id>', methods=['POST', 'GET'])
def pet_page_and_edit_pet(pet_id):
  '''This will show the user the pet they selected and will allow for the details to be edited'''
  form = AddPetFrom()
  pet = Pet.query.get(pet_id)

  # If the form submits the changes will be saved to the DB
  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data

    pet.name = name
    pet.species = species
    pet.photo_url = photo_url
    pet.age = age
    pet.notes = notes
    pet.available = available
    db.session.commit()
    return redirect('/')

  # Otherwise the pet's info page with the edit form will appear
  else:
    form.name.data = pet.name
    form.species.data = pet.species
    form.photo_url.data = pet.photo_url
    form.age.data = pet.age
    form.notes.data = pet.notes
    form.available.data = pet.available
    return render_template('pet_page.html', form = form, pet = pet)