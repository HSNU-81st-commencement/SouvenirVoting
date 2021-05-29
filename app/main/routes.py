from os import listdir
from flask import render_template, redirect, request, make_response, flash
from werkzeug.wrappers import response
from ..db import db
from ..forms import VoteForm, PersonalDataForm
from ..pages import pages
from . import main_bp


@main_bp.before_app_first_request
def db_check():
    if "data.db" not in listdir("../"):
        db.create_all()


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main_bp.route("/personal_data", methods=["GET", "POST"])
def personal_data_page():
    form = PersonalDataForm()
    if request.method == "GET":
        return render_template("personal_data.html", form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            response = make_response(redirect("/vote/1"))
            response.set_cookie("student_id",  str(form.student_id.data))
            response.set_cookie("classnum", str(form.classnum.data))
            return response
        else:
            for _, errorMessages in form.errors.items():
                for err in errorMessages:
                    flash(err, category="alert")
            return render_template("personal_data.html", form=form)


@main_bp.route("/vote/", methods=["GET", "POST"])
@main_bp.route("/vote/<int:page>", methods=["GET", "POST"])
def vote_page(page=1):
    form = VoteForm()
    form.choice.choices = pages[page]
    if request.method == "GET":
        return render_template(
            "vote_base.html",
            form=form,
        )
    if request.method == "POST":
        if form.validate_on_submit():
            choice = form.choice.data
            response = make_response(redirect("/vote/%d" % (page + 1)))
            response.set_cookie(page, choice)
        else:
            flash("Error", category="alert")
            return render_template(
                "vote_base.html",
                form=form,
            )


@main_bp.route("/end", methods=["GET"])
def process_all():
    # process
    return render_template("end.html")
