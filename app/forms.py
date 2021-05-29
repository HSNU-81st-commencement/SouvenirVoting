from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
    choice = SelectField("", validators=[DataRequired()])
    submit = SubmitField("送出")