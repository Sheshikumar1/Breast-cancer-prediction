# import Flask class and render_template
# An instance of this class will be our WSGI application.
from re import X
from flask import Flask
from flask.templating import render_template
from flask import request, url_for
import pickle
import numpy as np
import pandas as pd



# create an object of the class "Flask" by passing first argument.
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



# use the route() decorator to tell Flask what URL should trigger our function.
# argument here is pattern of url 
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index2.html", methods = ["POST"]) 
def predict():
    input_features = [float(X) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['mean texture', 'mean area', 'mean smoothness', 'mean concavity',
       'texture error', 'area error', 'worst texture', 'worst smoothness',
       'worst compactness', 'worst symmetry']

    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)   

    return render_template("index1.html", data=output)

   

if __name__=="__main__": 
    app.run(debug=True)