from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Get your guaiaca ready, \'cuz we\'re about to fill\'er up!"
