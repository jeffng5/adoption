from app import app
from models import Pet, db 

db.drop_all()
db.create_all()

db.session.commit()