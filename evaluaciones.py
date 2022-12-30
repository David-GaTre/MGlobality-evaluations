from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  
  #### Return a rendered index.html file
  return render_template('index.html')

@app.route("/cliente/<int:id>")
def client(id):
    pass
  #return render_template('fried_egg.html')