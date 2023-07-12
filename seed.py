from app import create_app
from app.model import db, Pet

app = create_app('Config')
app.app_context().push()

# Create the pets and add them to the database


def seed_pets():
    pets = [
        {
            'name': 'Fluffy',
            'species': 'Dog',
            'age': 2,
            'notes': 'Friendly and playful',
            'photo_url': "https://images.pexels.com/photos/2248516/pexels-photo-2248516.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            'available': True
        },
        {
            'name': 'Spot',
            'species': 'Dog',
            'age': 5,
            'notes': 'Independent and curious',
            'photo_url': "https://images.pexels.com/photos/7514959/pexels-photo-7514959.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            'available': True
        },
        {
            'name': 'Garfield',
            'species': 'Cat',
            'age': 5,
            'notes': 'Friendly, independent, funny',
            'photo_url': "https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg",
            'available': True
        },
        {
            'name': 'Rex',
            'species': 'Dog',
            'age': 3,
            'notes': 'Energetic, playful, and obedient',
            'photo_url': "https://images.pexels.com/photos/159692/dog-training-joy-fun-159692.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            'available': True
        },
        {
            'name': 'Sam',
            'species': 'Dog',
            'age': 9,
            'notes': 'Active and friendly',
            'photo_url': "https://images.pexels.com/photos/15347387/pexels-photo-15347387/free-photo-of-a-dog-in-close-up-shot.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            'available': True
        },
    ]

    for pet_data in pets:
        pet = Pet(**pet_data)
        db.session.add(pet)

    db.session.commit()


# Call the seed_pets function to insert the pets into the database
seed_pets()
