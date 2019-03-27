import os
from flask import Flask, render_template
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
db = MongoEngine(app)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
