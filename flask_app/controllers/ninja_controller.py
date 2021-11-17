from flask import render_template, redirect, session, request

from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route("/ninjas")
def add_ninja():
    return render_template("ninjas.html", all_dojos = Dojo.get_all())

@app.route("/ninjas/create", methods = ["POST"])
def create_ninjas():
    id = request.form['dojo_id']
    Ninja.create(request.form)
    return redirect(f"/dojos/{id}")

@app.route("/dojos/<id>")
def display_dojo(id):
    all_ninjas = Ninja.get_all()
    return render_template("dojo_show.html", dojo = Dojo.get_one({"id": id}), all_ninjas = Ninja.get_all())

