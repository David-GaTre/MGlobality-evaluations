from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
  #### Add a validator argument in the StringField
  # my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), ("id2","Two"), ("id3","Three")])
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Agregar Comentario")