from flask import render_template, request, redirect, url_for
from forms import CommentForm
from app import app, db # also enlist models needed

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
    #review = Review.query.filter_by(id=review_id).first_or_404(description='xd')

  #return render_template('cliente.html')