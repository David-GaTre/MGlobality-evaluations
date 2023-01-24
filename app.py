from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app) #database instance
# To create everything is with db.create_all()
migrate = Migrate(app, db)

@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

import routes