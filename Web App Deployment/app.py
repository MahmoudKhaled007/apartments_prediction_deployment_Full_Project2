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
    area = int(all_data['Area'])
    furnished = int(all_data['Datetime'])
    down_payment = int(all_data['Down_payment'])
    electricity_meter = int(all_data['Electricity_Meter'])
    balcony = int(all_data['Balcony'])
    water_meter = int(all_data['Water_Meter'])
    elevator = int(all_data['Elevator'])
    security = int(all_data['Security'])
    landline = int(all_data['Landline'])
    pets_allowed = int(all_data['Pets_Allowed'])
    covered_parking = int(all_data['Covered_Parking'])
    private_garden = int(all_data['Private_Garden'])
    natural_gas = int(all_data['Natural_Gas'])
    pool = int(all_data['Pool'])
    maids_room = int(all_data['Maids_Room'])
    central_ac_heating = int(all_data['Central_Ac_Heating'])
    built_in_kitchen_appliances = int(all_data['Built_In_Kitchen_Appliances'])
    location = location_dummies[all_data['Location']]
    compound = compound_dummies[all_data['Compound']]
    bedrooms = bedrooms_dummies[all_data['Bedrooms']]
    level = level_dummies[all_data['Level']]
    bathrooms = bathrooms_dummies[all_data['Bathrooms']]
    payment_option = payment_option_dummies[all_data['Payment_Option']]
    delivery_term = delivery_term_dummies[all_data['Delivery_Term']]
    delivery_date = delivery_date_dummies[all_data['Delivery_Date']]
    price_type=price_type_dummies[all_data['Price_Type']]
    month=month_dummies[all_data['Month']]
    x = [price , area , furnished , down_payment , electricity_meter , balcony , water_meter , elevator , security , natural_gas , landline , pets_allowed , covered_parking , private_garden , pool , maids_room , central_ac_heating , built_in_kitchen_appliances]
    x += location + compound + bedrooms + month + level + bathrooms + payment_option + delivery_term + delivery_date + price_type, month


    x = scaler.transform([x])
    meterprice = round(model.predict(x)[0])
    price=meterprice*area
    return render_template('prediction.html', meterprice=meterprice)

    







if __name__ == "__main__":
    app.run()