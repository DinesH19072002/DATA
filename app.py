from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)

model=pickle.load(open("model/model.pkl",'rb'))

scaler=pickle.load(open("model/scaler.pkl,'rb'))

@app.route