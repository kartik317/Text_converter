from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class IOForm(FlaskForm):
    input_text = StringField("Input", validators=[DataRequired()], widget=TextArea())
    
    output_text = StringField("Output", widget=TextArea())
    
    submit = SubmitField("Convert")