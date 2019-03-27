import os
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
# Debugger Toolbar
app.debug = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
toolbar = DebugToolbarExtension(app)
# MongoDB initialization
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
app.config['DEBUG_TB_PROFILER_ENABLED'] = True # Enable the profiler on all requests
db = MongoEngine(app)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
