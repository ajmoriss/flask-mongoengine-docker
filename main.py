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
# Available panels at the debugger toolbar
app.config['DEBUG_TB_PANELS'] = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    'flask_mongoengine.panels.MongoDebugPanel',
]
app.config['DEBUG_TB_PROFILER_ENABLED'] = True # Enable the profiler on all requests

db = MongoEngine(app)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
