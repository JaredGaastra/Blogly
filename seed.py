from models import db, Users, Posts, Tags, PostTag
from app import app

db.drop_all()
db.create_all()


user1 = Users(first_name="John", last_name="Smith", image_url="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")
user2 = Users(first_name="Jane", last_name="Doe", image_url="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")
user3 = Users(first_name="Bob", last_name="Smith", image_url="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")
user4 = Users(first_name="Sally", last_name="Smith", image_url="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")
user5 = Users(first_name="Joe", last_name="Smith", image_url="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")

db.session.add_all([user1, user2, user3, user4, user5])
db.session.commit()

post1 = Posts(title="First Post", content="This is the first post", user_id=1)
post2 = Posts(title="Second Post", content="This is the second post", user_id=1)
post3 = Posts(title="Third Post", content="This is the third post", user_id=2)
post4 = Posts(title="Fourth Post", content="This is the fourth post", user_id=3)
post5 = Posts(title="Fifth Post", content="This is the fifth post", user_id=4)

db.session.add_all([post1, post2, post3, post4, post5])
db.session.commit()


tag1 = Tags(name="fun", id=1)
tag2 = Tags(name="happy", id=2)
tag3 = Tags(name="sad", id=3)
tag4 = Tags(name="mad",     id=4)
tag5 = Tags(name="excited", id=5)

db.session.add_all([tag1, tag2, tag3, tag4, tag5])
db.session.commit()




