from flask import Flask, render_template, request
app = Flask('app')

classes = [
  'Guerrier',
  'Paladin',
  'Roublard',
  'Voleur',
  'Mage',
  'Archer'
]

personnages = []

@app.route('/')
@app.route('/main')
def main():
  return render_template('main.html', classes = classes)

@app.route('/liste')
def liste():
  global personnages
  return render_template('liste.html', liste = personnages)

@app.route('/ficheDepuisListe', methods = ['POST'])
def ficheDepuisListe() :
  perso = None
  for e in personnages :
    if e['nom'] == request.form["nom"] :
      perso = e
      break
  print(perso)
  return afficherFiche(perso)

@app.route('/fiche', methods = ['POST'])
def fiche() :
  dico = {key : value for key, value in request.form.items()}
  return afficherFiche(dico)

def afficherFiche(perso) :
  return render_template('fiche.html', perso = perso)

@app.route('/nouveau')
def nouveau():
  return render_template('nouveau.html', classes = classes)

@app.route('/ajouter', methods = ['POST'])
def ajouter() :
  global personnages
  dico = {}
  for key, value in request.form.items() :
    dico[key] = value
  personnages += [dico]
  return afficherFiche(dico)

app.run(host='localhost', port=8080)