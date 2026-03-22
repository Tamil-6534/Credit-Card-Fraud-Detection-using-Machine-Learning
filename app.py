from flask import request,render_template,Flask
import pickle

app=Flask(__name__)

scalar=pickle.load(open('scalar.pkl','rb'))
classification=pickle.load(open('classification.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

import pandas as pd

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(x) for x in request.form.values()]

    columns = ['Amount','V6','V1','V5','V7','V20','V12','V22','V4','V11','V21']
    
    new_data = pd.DataFrame([values], columns=columns)

    new_data['Amount'] = scalar.transform(new_data[['Amount']])

    prediction = classification.predict(new_data)

    output = "Fraud Transaction ❌" if prediction[0] == 1 else "Normal Transaction ✅"

    return render_template('index.html', prediction_text=output)

if __name__=='__main__':
    app.run(debug=True)