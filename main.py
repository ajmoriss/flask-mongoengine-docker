import os
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# Debugger Toolbar
app.debug = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG_TB_PROFILER_ENABLED'] = True # Enable the profiler on all requests
toolbar = DebugToolbarExtension(app)
# MongoDB initialization
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
db = MongoEngine(app)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
