from flask import render_template, redirect, request, make_response, flash
from ..forms import VoteForm
from ..pages import pages
from . import main_bp


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main_bp.route("/vote/", methods=["GET", "POST"])
@main_bp.route("/vote/<int:page>", methods=["GET", "POST"])
def vote_page(page=1):
    form = VoteForm()
    form.choice.choices = pages[page]
    if request.method == "GET":
        return render_template(
            "vote_base.html",
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
            )


@main_bp.route("/end", methods=["GET"])
def process_all():
    # process
    return render_template("end.html")
