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
    print(p)
    out = {'Prediction': p}
    return out


if __name__=='__main__':
    app.run(debug=True)










# =============================================================================
# class Predict(Resource):
# 
#     @staticmethod
#     def post():
#         parser = reqparse.RequestParser()
#         parser.add_argument('year')
#         parser.add_argument('month')
#        
#         args = parser.parse_args()  # creates dict
# 
#         X_new = args.keys()  # convert input to array
# 
#         out = {'Prediction': MODEL.predict('%s-%s' % (X_new))}
# 
#         return out, 200
# 
# 
# API.add_resource(Predict, '/predict')
# 
# if __name__ == '__main__':
#     APP.run(debug=True, port='1080')
#     
# =============================================================================
    
    
# model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[2, 9, 6]]))