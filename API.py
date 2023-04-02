from flask import Flask , jsonify , request

import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)

def trans(p):
    le = LabelEncoder()
    p.Sex = le.fit_transform(p.Sex)
    p.Housing = le.fit_transform(p.Housing)
    p.Saving_accounts = le.fit_transform(p.Saving_accounts)
    p.Checking_account = le.fit_transform(p.Checking_account)
    p.Purpose = le.fit_transform(p.Purpose)
    x = np.array(p)
    return x

DT = joblib.load('model.pkl')

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['POST'])
def predict():
     print(request.get_json())
     json_ = request.get_json()
     for k,v in json_.items():
         if type(v) != float and type(v) != str :
             v = int(v)
         json_[k] = [v]
     query_df = pd.DataFrame(json_)
     query = trans(query_df)
     prediction = DT.predict(query)
     if(prediction == 1):
         rsult="Good"
     else:
         rsult="Bad"
     return jsonify({'prediction': rsult})

if __name__ == '__main__':
    app.run(debug=True)
