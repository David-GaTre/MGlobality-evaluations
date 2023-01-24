from app import app, db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), unique = True, index = True)
  password_hash = db.Column(db.String(128))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

#declaring the Book model
#class Book(db.Model):
#    id = db.Column(db.Integer, primary_key = True) #primary key column
#    title = db.Column(db.String(80), index = True, unique = True) # book title
#    author_name = db.Column(db.String(50), index = True, unique = False)
#    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
#    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
#    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
#    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') #relationship of Books and Reviews
    
    #Get a nice printout for Book objects
#    def __repr__(self):
#        return "{} in: {},{}".format(self.title, self.month, self.year)

#Add your columns for the Reader model here below.
#class Reader(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    name = db.Column(db.String(50), index = True, unique = False)
#    surname = db.Column(db.String(80), unique = False, index = True)
##    email = db.Column(db.String(120), unique = True, index = True)
 #   reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')
  
    #get a nice printout for Reader objects
#    def __repr__(self):
#        return "Reader: {}".format(self.email)

#declaring the Review model
#class Review(db.Model):
#    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
#    stars = db.Column(db.Integer, unique = False) #a review's rating
#    text = db.Column(db.String(200), unique = False) #a review's text
    #here below is the foreign key column linking to the primary key (id) of the Book model (book). 
    #Note the lower case here: 'book.id' instead of 'Book.id'
#    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
    #your code here
#    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'), cascade = 'all, delete, delete-orphan')
    #get a nice printout for Review objects
#    def __repr__(self):
#        return "Review: {} stars: {}".format(self.text, self.stars)

# add data
#db.session.add(new_reader1)
#try:
#    db.session.commit()
#except:
#    db.session.rollback()