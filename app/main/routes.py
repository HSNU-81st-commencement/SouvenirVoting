from os import listdir
from datetime import datetime
from flask import (
    render_template,
    redirect,
    request,
    make_response,
    flash,
    abort,
    current_app,
)
from .. import log
from ..db import db
from ..forms import VoteForm, PersonalDataForm
from ..data import pages
from . import main_bp
from .db_helper import add_record


@main_bp.before_app_first_request
def db_check():
    if "data.db" not in listdir("../"):
        db.create_all()


@main_bp.route("/", methods=["GET"])
def index():
    log(request)
    return render_template("index.html")


@main_bp.route("/personal_data", methods=["GET", "POST"])
def personal_data_page():
    log(request)
    form = PersonalDataForm()
    if request.method == "GET":
        return render_template("personal_data.html", form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            response = make_response(redirect("/vote/1"))
            response.set_cookie("student_id", str(form.student_id.data))
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
    log(request)
    form = VoteForm()
    form.choices.choices = pages[page - 1]
    if page != 1:
        abort(404)
    if request.method == "GET":
        return render_template(
            "vote_base.html",
            page=page,
            form=form,
        )
    if request.method == "POST":
        if form.validate_on_submit():
            choice = form.choices.data
            if page == len(pages):
                response = make_response(redirect("/end"))
            else:
                response = make_response(redirect("/vote/%d" % (page + 1)))
            response.set_cookie(str(page), choice)
            return response
        else:
            flash("Error", category="alert")
            return redirect("/vote/%d" % page)


@main_bp.route("/end", methods=["GET"])
def process_all():
    log(request)
    student_id = request.cookies.get("student_id")
    classnum = request.cookies.get("classnum")
    votes = dict()
    for i in range(1, 9):  # 8 items
        votes[i] = request.cookies.get(str(i))
    if not (all(votes.values()) and student_id and classnum):
        flash("資料不完整，請重新填寫", category="alert")
    else:
        add_record(student_id, classnum, votes)
        flash("你已完成投票", category="success")
    return render_template("end.html")
