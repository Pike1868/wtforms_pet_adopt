from flask import Blueprint, render_template, redirect, request, flash, url_for
from .model import db, Pet
from .forms import PetForm, EditPetForm

main = Blueprint('main', __name__)


@main.route("/")
def show_homepage():
    """Show homepage"""
    pets = Pet.query.order_by(Pet.name.asc()).all()

    return render_template("index.html", pets=pets)


@main.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """Show form to add pets and handle form submission"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()

        flash("Pet added successfully")
        return redirect(url_for("main.show_homepage"))
    elif request.method == 'POST':
        flash("Error adding pet, please check inputs")

    return render_template("add_pet_form.html", form=form)


@main.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect(url_for("main.show_homepage"))
    elif request.method == 'POST':
        flash("Error editing pet, please check your inputs")

    return render_template("pet_details.html", pet=pet, form=form)
