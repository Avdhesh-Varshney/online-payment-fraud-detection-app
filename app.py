from flask import Flask, render_template, request
import numpy as np
import joblib

model = joblib.load('model.joblib')

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    trans_type = request.form['type']
    amount = request.form['amount']
    oldbalanceOrg = request.form['oldbalanceOrg']
    newbalanceOrig = request.form['newbalanceOrig']
    arr = np.array([[int(trans_type), float(amount), float(oldbalanceOrg), float(newbalanceOrig)]])

    pred = model.predict(arr)
    return render_template('index.html', prediction_text=pred[0])

if __name__ == '__main__':
    app.run(debug=True)
