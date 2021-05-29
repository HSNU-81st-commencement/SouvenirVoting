from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class PersonalDataForm(FlaskForm):
    student_id = IntegerField(
        "",
        validators=[DataRequired(), NumberRange(min=700000, max=1000000)],
        render_kw={"placeholder": "學號"},
    )
    classnum = IntegerField(
        "",
        validators=[DataRequired(), NumberRange(min=1478, max=1600)],
        render_kw={"placeholder": "原班級"},
    )
    submit = SubmitField("送出")

    # TODO validate student_id and classnum


class VoteForm(FlaskForm):
    choice = SelectField(
        "", validators=[DataRequired()], render_kw={"placeholder": "選擇"}
    )
    submit = SubmitField("送出")
