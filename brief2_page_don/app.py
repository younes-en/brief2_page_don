
from flask import Flask, render_template, request
import data

app = Flask(__name__)

@app.route('/')
def index() :
    datas = data.get_users()
    return render_template('index.html', utilisateurs = datas)
 
@app.route('/donnateur')
def donnateur():
    utilisateur = data.get_users()
    total = data.total_dons()
    return render_template('donnateur.html', quelquun=utilisateur, total=total) 
 
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/add', methods=['post'])
def add():
     
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    adresse = request.values.get('adresse')
    mail = request.values.get('mail')
    somme = request.values.get('somme')

    data.set_utilisateur(nom, prenom, adresse, mail, somme)
    
    return render_template('add.html' )  
 
if __name__== "__main__" :
        app.run(debug=True, port=5001) 


 