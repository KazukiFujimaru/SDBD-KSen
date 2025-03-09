from flask import render_template
from modules import modules

def configure_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/testpg")
    def testpg():
        return render_template("testpg.html")