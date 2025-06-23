from app import create_app, db
from models import User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    print("Clearing db...")
    db.drop_all()
    db.create_all()

    print("Creating users ...")
    user1 = User(username='alice')
    user1.password = 'password123'

    user2 = User(username='bob')
    user2.password = 'securepass'

    db.session.add_all([user1, user2])
    db.session.commit()

    print("Creating guests...")
    guest1 = Guest(name='John Doe', occupation='Comedian')
    guest2 = Guest(name='Jane Smith', occupation='Scientist')

    db.session.add_all([guest1, guest2])
    db.session.commit()

    print("Creating episodes...")
    episode1 = Episode(date='2023-06-01', number=1)
    episode2 = Episode(date='2023-06-08', number=2)

    db.session.add_all([episode1, episode2])
    db.session.commit()

    print("Creating appearances...")
    appearance1 = Appearance(rating=4, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=3, guest_id=guest2.id, episode_id=episode2.id)

    db.session.add_all([appearance1, appearance2])
    db.session.commit()

    print("Seeded database successfully!")
