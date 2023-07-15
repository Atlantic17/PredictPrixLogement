from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='html')

# Charger le modèle de prédiction
model = pd.read_pickle('model.pkl')

# Charger les statistiques de base pour la normalisation des données
#scaler = StandardScaler()
#scaler.mean_ = pd.read_pickle('mean.pkl')
#scaler.var_ = pd.read_pickle('var.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les données saisies par l'utilisateur
    f1 = request.form['position']
    f2 = request.form['nbchambres']
    f3 = request.form['douche_interne']
    f4 = request.form['douche_externe']
    f5 = request.form['cuisine_externe']
    f6 = request.form['cuisine_interne']
    # Vérifier chaque champ individuellement
    error = False
    if not f1:
        error = True
        error_position = "Veuillez remplir ce champ."
    else:
        f1 = float(f1)
        error_position = None

    if not f2:
        error = True
        error_nbchambres = "Veuillez remplir ce champ."
    else:
        f2 = float(f2)
        error_nbchambres = None

    if not f3:
        error = True
        error_douche_interne = "Veuillez remplir ce champ."
    else:
        f3 = float(f3)
        error_douche_interne = None

    if not f4:
        error = True
        error_douche_externe = "Veuillez remplir ce champ."
    else:
        f4 = float(f4)
        error_douche_externe = None

    if not f5:
        error = True
        error_cuisine_externe = "Veuillez remplir ce champ."
    else:
        f5 = float(f5)
        error_cuisine_externe = None

    if not f6:
        error = True
        error_cuisine_interne = "Veuillez remplir ce champ."
    else:
        f6 = float(f6)
        error_cuisine_interne = None

    # Si un champ est manquant, renvoyer le modèle HTML avec les messages d'erreur
    if error:
        return render_template('index.html', error_position=error_position, error_nbchambres=error_nbchambres,
                               error_douche_interne=error_douche_interne, error_douche_externe=error_douche_externe,
                               error_cuisine_externe=error_cuisine_externe, error_cuisine_interne=error_cuisine_interne)
    else:
    # Normaliser les données saisies par l'utilisateur
         data = [[f1, f2, f3, f4, f5, f6]]
    #data = scaler.transform([[f1, f2, f3, f4, f5, f6]])

     # Effectuer la prédiction avec le modèle
         prediction = int(model.predict(data)[0])

     #return 'Prediction: {}'.format(prediction)

         return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

