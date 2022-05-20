from models import db, Pet
from app import app

# create all tables
db.drop_all()
db.create_all()

# If table isnt empty then empty it
Pet.query.delete()

# Add different pet entries
bingo = Pet(name = 'Bingo', 
species = 'dog', 
photo_url = 'https://images.pexels.com/photos/5255253/pexels-photo-5255253.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
age = 3, 
notes = 'Super friendly and energetic puppy with a lot of love to give.')

bella = Pet(name = 'Bella', 
species = 'cat', 
photo_url = 'https://images.pexels.com/photos/1629061/pexels-photo-1629061.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
age = 1, 
notes = 'Cuddly kitten looking for a place to call home')

baby = Pet(name = 'Baby', 
species = 'bird', 
photo_url = 'https://images.pexels.com/photos/7455192/pexels-photo-7455192.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 
notes = 'A chattering parakeet looking for a shoulder to perch on')

ruffus = Pet(name = 'Ruffus', 
species = 'hamster', 
photo_url = 'https://images.pexels.com/photos/3362697/pexels-photo-3362697.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 
age = 2,
notes = 'A fluffy hamster looking for a budy',
available = False)
 
db.session.add(bingo)
db.session.add(bella)
db.session.add(baby)
db.session.add(ruffus)

db.session.commit()