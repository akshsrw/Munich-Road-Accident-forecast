# app.py
from flask import Flask,request
import json
import pickle

app= Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict',methods=['POST'])

def predict():
    event= json.loads(request.data)
    Month=event['month']
    Year=event['year']
    p=int(model.forecast('%s-%s' % (Year,Month))[-1])
    out = {'Prediction': p}
    return out


if __name__=='__main__':
    app.run(debug=True)



