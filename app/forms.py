from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class PersonalDataForm(FlaskForm):
    student_id = DecimalField(
        "",
        validators=[
            DataRequired(message="請填學號"),
            NumberRange(min=700000, max=1000000, message="請填正確學號"),
        ],
        render_kw={"placeholder": "學號"},
    )
    classnum = DecimalField(
        "",
        validators=[
            DataRequired(message="請填原班級"),
            NumberRange(min=1478, max=1553, message="請填正確班號"),
        ],
        render_kw={"placeholder": "原班級"},
    )
    submit = SubmitField("送出")


class VoteForm(FlaskForm):
    choices = SelectField("", validators=[DataRequired()])
    submit = SubmitField("送出")
