from flask import render_template
from modules import modules

def configure_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/testpg")
    def testpg():
        return render_template("testpg.html")
    
    @app.route("/elements")
    def elements():
        return render_template("elements.html")
    
    @app.route("/materi/p1")
    def pertemuan1():
        return render_template("materi1.html")
    
    @app.route("/materi/p2")
    def pertemuan2():
        return render_template("materi2.html")
    
    @app.route("/materi/p3")
    def pertemuan3():
        return render_template("materi3.html")
    
    @app.route("/test2")
    def test2():
        return render_template("testpg2.html")