from flask import render_template, redirect, session, request

from flask_app import app
from flask_app.models.dojos import Dojo


@app.route("/dojos")
def index():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojo.html", all_dojos = all_dojos)


@app.route("/dojo/create", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)
    print(request.form)
    return redirect("/dojos")


@app.route("/dojo/<id>/edit")
def edit(id):
    return render_template("edit_dojo.html", dojo = Dojo.get_one({"id": id}))


@app.route("/dojo/<id>/update", methods = ["POST"])
def update_dojo(id):
    print(request.form)
    data = {
        **request.form,
        "id": id
    }
    Dojo.update(data)
    return redirect(f"/dojo/{id}")



