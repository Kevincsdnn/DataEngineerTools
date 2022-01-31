from socketserver import DatagramRequestHandler
from flask import Flask, render_template, jsonify, url_for
import json
from app.lefigaro import *
from app.lemonde import *

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('homepage.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/hello/')
    @app.route('/hello/<name>/')
    def hello(name='Marius'):
        return render_template('hello.html', name=name)



    @app.route('/articles_lefigaro/')
    @app.route('/articles_lefigaro/<nbr>/')
    def articles_lefigaro(nbr=1):
        nombre = int(nbr)
        data = fonction2("https://www.lefigaro.fr/elections/presidentielles",nombre)
        titres=[]
        descriptions=[]
        liens=[]
        taille = len(data)
        for i in range (taille) :
            titres+= [data[i]['Title']]
            descriptions += [data[i]['Description']]
            liens+= [data[i]['Lien']]
        
        return render_template('lefigaro.html',nombre=nombre,taille=taille,titres=titres,descriptions=descriptions,liens=liens)

    @app.route('/articles_lemonde/')
    def articles_lemonde():
        data = fonctionb("https://www.lemonde.fr/election-presidentielle-2022/")
        titres=[]
        descriptions=[]
        liens=[]
        taille = len(data)
        for i in range (taille) :
            titres+= [data[i]['Title']]
            descriptions += [data[i]['Description']]
            liens+= [data[i]['Lien']]
        
        return render_template('lemonde.html',taille=taille,titres=titres,descriptions=descriptions,liens=liens)

    @app.route('/sondages/')
    def sondages():
        return render_template('sondages.html')
        

    return app