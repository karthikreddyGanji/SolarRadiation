from flask import Flask, render_template, request
import joblib
import pickle
import numpy as np
#from datetime import datetime
#from sklearn.ensemble import ExtraTreesRegressor


app = Flask(__name__)

@app.route('/')
@app.route('/main_template', methods=["GET"])
def main_template():
    return render_template('index1.html')
def convert_time_to_seconds(time_str):
    time_components = [int(component) for component in time_str.split(':')]
    return time_components[0] * 3600 + time_components[1] * 60 + time_components[2]

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        #date_str = request.form['Date']
        #date_object = datetime.strptime(date_str, '%Y-%m-%d')
        #date = date_object.timestamp()
        time_str = request.form['Time']
        time = convert_time_to_seconds(time_str)
        time_str = request.form['TimeSunRise']
        timesunrise = convert_time_to_seconds(time_str)
        time_str = request.form['TimeSunSet']
        timesunset = convert_time_to_seconds(time_str)

        features = [
            time,
            float(request.form['Temperature']),
            float(request.form['Pressure']),
            float(request.form['Humidity']),
            float(request.form['WindDirection']),
            timesunrise,
            timesunset,
            
        ]

        features = np.array(features).reshape(1, -1)
        prediction = m.predict(features)[0]
        prediction=round(prediction,2)
        
        print("Prediction:", prediction)
        return render_template('result1.html', prediction=prediction)

if __name__== '__main__':
    m = joblib.load(r"C:\Users\karth\Desktop\solarproject\mymodel.pkl")
    app.run(host="0.0.0.0",port=5000,debug=True)