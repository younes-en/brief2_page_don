import mysql.connector as msql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='root', password='root', host='localhost', port="8081", database='dons')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_users() :
    global cursor

    connexion()
    query = "SELECT * FROM utilisateurs"
    cursor.execute(query)
    utilisateurs = []

    for enregistrement in cursor :
        post = {}
        post['id'] = enregistrement[0]
        post['nom'] = enregistrement[1]
        post['prenom'] = enregistrement[2]
        post['adresse'] = enregistrement[3]
        post['mail'] = enregistrement[4]
        post['somme'] = enregistrement[5]
        utilisateurs.append(post)
    
    print(utilisateurs)
    deconnexion()
    return utilisateurs
def get_user():
    global cursor

    connexion()
    query = "SELECT * FROM utilisateurs" 
    cursor.execute(query)
    form = {}

    for enregistrement in cursor :
        form['id'] = enregistrement[0]
        form['nom'] = enregistrement[1]
        form['prenom'] = enregistrement[2]
        form['adresse'] = enregistrement[3]
        form['mail'] = enregistrement[4]
        form['somme'] = enregistrement[5]

    deconnexion()
    return form

def total_dons() :
    global bdd
    global cursor

    connexion()
    query = "SELECT somme FROM utilisateurs"
    cursor.execute(query)
    total=0

    for enregistrement in cursor : 
        total += enregistrement[0]


    
    deconnexion()
    return total
 
def set_utilisateur(nom, prenom, adresse, mail, somme):
    global bdd
    global cursor

    connexion()

    query='INSERT INTO utilisateurs(nom, prenom, adresse, mail, somme) VALUES ("'+nom+'","'+prenom+'","'+adresse+'","'+mail+'","'+somme+'");'
    cursor.execute(query)
    bdd.commit()

    deconnexion() 
 