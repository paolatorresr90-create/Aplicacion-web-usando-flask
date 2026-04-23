from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Cargamos el modelo XGBoost
model = pickle.load(open('wine_model_xgb.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capturamos los datos en el ORDEN EXACTO del entrenamiento
    # 1. Alcohol, 2. Volatile Acidity, 3. Sulphates, 4. Citric Acid, 5. Total Sulfur Dioxide
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    
    prediction = model.predict(final_features)
    
    res_text = "¡Excelente elección! Es un vino de alta calidad." if prediction[0] == 1 else "Es un vino de calidad promedio."
    
    return render_template('index.html', prediction_text=res_text)

if __name__ == "__main__":
    app.run(debug=True)