from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
  #### Add a validator argument in the StringField
  # my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), ("id2","Two"), ("id3","Three")])
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Agregar Comentario")

class FieldsRequiredForm(FlaskForm):
  """Require radio fields to have content. This works around the bug that WTForms radio fields don't honor the `DataRequired` or `InputRequired` validators."""
  class Meta:
    def render_field(self, field, render_kw):
      if field.type == "_Option":
        render_kw.setdefault("required", True)
      return super().render_field(field, render_kw)

categories = [("recommended","Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")]