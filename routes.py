from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from forms import CommentForm, RegistrationForm, LoginForm
from app import app, db
from models import *  # Only enlist the used models
from flask import render_template, request, url_for, redirect, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user



login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
  # do stuff
  return "Sorry you must be logged in to view this page"

@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user)
      render_template('index.html', current_user = user)
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))


@app.route("/cliente/<int:id>", methods=['GET', 'POST'])
@login_required
def client(id):
    if request.method == 'POST':
        comment_form = CommentForm(csrf_enabled=False)
        new_id = 2 # Placeholder
        if comment_form.validate_on_submit():
            pass
            # new_comment = comment_form.comment.data
            # comments[id].append(new_comment)
            # return redirect(url_for("almacen", id=new_id, _external=True, _scheme="https")) # for redirection those args are needed
            #review = Review.query.filter_by(id=review_id).first_or_404(description='xd')

        return render_template('cliente.html')
    return login_manager.unauthorized()

#@app.route('/profiles')
#def profiles():
#    current_users = User.query.all() #change here to a database query
#    return render_template('users.html', current_users = current_users)

#@app.route('/profile/<int:user_id>')
#def profile(user_id):
#   user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")
#   songs = Song.query.all()
#   my_playlist = None #change here to a database query
#   return render_template('profile.html', user = user, songs = songs, my_playlist = my_playlist)

#Adds new songs to a user's playlist from the song library
#redirects back to the profile that issued the addition
#app.route('/add_item/<int:user_id>/<int:song_id>/<int:playlist_id>')
#def add_item(user_id, song_id, playlist_id):
#   new_item = Item(song_id = song_id, playlist_id = playlist_id)
#   user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")
#   my_playlist = Playlist.query.filter_by(id = user.playlist_id).first()
#   if not exists(new_item, my_playlist.items):
#      song = Song.query.get(song_id)
#      #using db session add the new item
#      db.session.add(new_item)
#      #increase the counter for the song associated with the new item
#      song.n = song.n + 1
#      #commit the database changes here
#      try:
#        db.session.commit()
#      except:
#        db.session.rollback()
#   return redirect(url_for('profile', user_id = user_id))


#@app.route('/remove_item/<int:user_id>/<int:item_id>')
#def remove_item(user_id, item_id):
#   #from the Item model, fetch the item with primary key item_id to be deleted
#   item = Item.query.get(item_id)
#   #using db.session delete the item
#   db.session.delete(item)
#   #commit the deletion
#   db.session.commit()
#   return redirect(url_for('profile', user_id = user_id))

#@app.route('/dashboard', methods=["GET", "POST"])
#def dashboard():
#  form = SongForm()
#  if request.method == 'POST' and form.validate():
#    new_song = Song(title=form.title.data, artist=form.artist.data, n=1)
#    db.session.add(new_song)
#    db.session.commit()
#  else:
#        flash(form.errors)
#  unpopular_songs = Song.query.order_by(Song.n)  #add the ordering query here
#  songs = Song.query.all()
#  return render_template('dashboard.html', songs = songs, unpopular_songs = unpopular_songs, form = form)

# registration route
#@app.route('/register', methods=['GET', 'POST'])
#def register():
#  form = RegistrationForm(csrf_enabled=False)
#  if form.validate_on_submit():
#    user = User(username=form.username.data, email=form.email.data)
#    user.set_password(form.password.data)
#    db.session.add(user)
#    db.session.commit()
#  return render_template('register.html', title='Register', form=form)