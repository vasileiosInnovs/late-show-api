# seed.py

from app import app, db
from models import User, Episode, Guest, Appearance
from werkzeug.security import generate_password_hash

with app.app_context():
    print("Clearing db...")
    db.drop_all()
    db.create_all()

    print("Seeding users...")
    user1 = User(name="admin", _password_harsh=generate_password_hash("password123"))

    print("Seeding guests...")
    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Smith", occupation="Comedian")

    print("Seeding episodes...")
    episode1 = Episode(date="2023-06-15", number=1)
    episode2 = Episode(date="2023-06-22", number=2)

    print("Seeding appearances...")
    appearance1 = Appearance(episode=episode1, guest=guest1, rating=8.5)
    appearance2 = Appearance(episode=episode1, guest=guest2, rating=9.2)
    appearance3 = Appearance(episode=episode2, guest=guest2, rating=7.8)

    db.session.add_all([user1, guest1, guest2, episode1, episode2, appearance1, appearance2, appearance3])
    db.session.commit()

    print("Seeding complete!")