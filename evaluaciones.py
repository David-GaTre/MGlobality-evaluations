from flask import Flask, render_template, request, redirect, url_for
from forms import CommentForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
#db = SQLAlchemy(app) #database instance


@app.route('/')
def index():
  return render_template('index.html')

@app.route("/cliente/<int:id>")
def client(id):
    comment_form = CommentForm(csrf_enabled=False)
    new_id = 2 # Placeholder
    if comment_form.validate_on_submit():
      pass
      # new_comment = comment_form.comment.data
      # comments[id].append(new_comment)
      # return redirect(url_for("almacen", id=new_id, _external=True, _scheme="https")) # for redirection those args are needed
  #return render_template('cliente.html')