from flask import Flask, render_template, url_for,request
import pickle as p
import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



modelfile = 'models/final_prediction.pickle'  
model = p.load(open(modelfile, 'rb'))
scaler= pickle.load(open('models/scaler.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/predict',methods =['GET','POST'])
def predict():
    yummy = float(request.form["yummy"])
    convenient =float(request.form['convenient'])
    spicy = float(request.form['spicy'])
    fattening=float(request.form['fattening'])
    greasy = float(request.form['greasy'])
    fast  = float(request.form['fast'])
    cheap= float(request.form['cheap'])
    tasty =float(request.form['tasty'])
    expensive = float(request.form['expensive'])
    healthy=float(request.form['healthy'])
    disgusting = float(request.form['disgusting'])
    Age  = float(request.form['Age'])
    Gender= float(request.form['Gender'])
 

    total = [[yummy, convenient, spicy, fattening, greasy, fast, cheap,
       tasty, expensive, healthy, disgusting, Age, Gender]]
    prediction = model.predict(scaler.transform(total))
    prediction = int(prediction[0])

    if prediction==0:
        return render_template('index.html',predict="Predicts Customer belong to cluster 0")
    
    if prediction==1:
        return render_template('index.html',predict="Predicts Customer belong to cluster 1")
    if prediction==2:
        return render_template('index.html',predict="Predicts Customer belong to cluster 2")
    
    else: 
        return render_template('index.html',predict="Predicts Customer belong to cluster 3")
    


    




if __name__ == '__main__':
    app.run(debug=True)
