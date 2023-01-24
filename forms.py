from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

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

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])  
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])  
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')