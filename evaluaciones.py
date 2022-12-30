from flask import Flask, render_template, request, redirect, url_for
from forms import CommentForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

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
      # return redirect(url_for("almacen", id=new_id, _external=True, _scheme="https"))
  #return render_template('cliente.html')