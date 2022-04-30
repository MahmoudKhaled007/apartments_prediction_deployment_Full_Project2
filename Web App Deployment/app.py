from flask import Flask, render_template, request
from helpers.dummies import *
import joblib

app = Flask(__name__)

model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/predict', methods=['GET'])
def predict():
    all_data = request.args
    temp = float(all_data['temp'])
    humidity = float(all_data['humidity'])
    hour = int(all_data['datetime'].split('T')[1].split(':')[0])
    is_rush_hour = int(all_data['is_rush_hour'])
    location = location_dummies[all_data['location']]
    compound = compound_dummies[all_data['compound']]
    bedrooms = bedrooms_dummies[all_data['bedrooms']]
    level = level_dummies[all_data['level']]
    bathrooms = bathrooms_dummies[all_data['bathrooms']]
    payment_option = payment_option_dummies[all_data['payment_option']]
    delivery_term = delivery_term_dummies[all_data['delivery_term']]
    delivery_date = delivery_date_dummies[all_data['delivery_date']]
    price_type=price_type_dummies[all_data['price_type']]
    month=month_dummies[all_data['month']]
    x = [temp, humidity, hour, is_rush_hour]
    x += location + compound + bedrooms + month + level + bathrooms + payment_option + delivery_term + delivery_date + price_type, month


    x = scaler.transform([x])
    bikes_count = round(model.predict(x)[0])

    return render_template('prediction.html', bikes_count=bikes_count)









if __name__ == "__main__":
    app.run()