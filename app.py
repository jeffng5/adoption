from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
# from sqlalchemy import create_engine
from forms import AddPetForm


app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///recruitment'
app.config['SQLACLHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'nowayJose'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

@app.route('/', methods=['GET','POST'])
def home_page():
    entries = Pet.query.all()
    return render_template('home.html', entries=entries)


@app.route('/add', methods= ['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age= form.age.data
        notes = form.notes.data
        animal = Pet(name= name, species=species, age=age, notes=notes, photo_url=photo_url )
        db.session.add(animal)
        db.session.commit()
    
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)

@app.route("/<int:id>", methods=['GET','POST'])
def get_pet(id):
    
    pet= Pet.query.get_or_404(id)
    
    form = AddPetForm()
    user= Pet.query.get(id)
    if form.validate_on_submit():
        user.photo_url = form.photo_url.data
        user.notes = form.notes.data
        user.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        pet= Pet.query.get_or_404(id)
        return render_template("pet_detail.html", pet=pet, form=form)

    
