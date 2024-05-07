from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Act_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        
        # pickup Date
        date_pickup = request.form["Pickup_Time"]
        Journey_day = int(pd.to_datetime(date_pickup, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_pickup, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Weight
        Weight = request.form["Weight"]
        # print(Weight)
        
        # Vehicle Type
        # Vehicle Type = 0 (not in column)
        Vehicle_Type=request.form['Vehicle Type']
        if(Vehicle_Type=='Tata Ape'):
            Tata_Ape = 1
            Tata_Ace = 0
            Ashok_Leyland = 0
            Tata_407 = 0
            
            
        elif (Vehicle_Type=='Tata Ace'):
            Tata_Ape = 0
            Tata_Ace = 1
            Ashok_Leyland = 0
            Tata_407 = 0
        
        elif (Vehicle_Type=='Ashok Leyland'):
            Tata_Ape = 0
            Tata_Ace = 0
            Ashok_Leyland = 1
            Tata_407 = 0
        
        elif (Vehicle_Type=='Tata 407'):
            Tata_Ape = 0
            Tata_Ace = 0
            Ashok_Leyland = 0
            Tata_407 = 1
            
        else:
            Tata_Ape = 0
            Tata_Ace = 0
            Ashok_Leyland = 0
            Tata_407 = 0
            
        # print(Tata_Ape,
        #     Tata_Ace,
        #     Ashok_Leyland,
        #     Tata_407)
         
         # Pickup
        # Aariyur = 0 (not in column)
        Pickup_Location = request.form["Pickup_Location"]
        if (Pickup_Location == 'Agaram Chithamoor'):
            p_Agaram_Chithamoor = 1
            p_Kalpattu = 0
            p_Kanai = 0
            p_Kangiyanoor = 0
            
        elif (Pickup_Location == 'Kalpattu'):
            p_Agaram_Chithamoor = 0
            p_Kalpattu = 1
            p_Kanai = 0
            p_Kangiyanoor = 0
            
        elif (Pickup_Location == 'Kanai'):
            p_Agaram_Chithamoor = 0
            p_Kalpattu = 0
            p_Kanai = 1
            p_Kangiyanoor = 0
            
        elif (Pickup_Location == 'Kangiyanoor'):
            p_Agaram_Chithamoor = 0
            p_Kalpattu = 0
            p_Kanai = 0
            p_Kangiyanoor = 1
            
        else:
            p_Agaram_Chithamoor = 0
            p_Kalpattu = 0
            p_Kanai = 0
            p_Kangiyanoor = 0
            
        # print(p_Agaram_Chithamoor,
        #     p_Kalpattu,
        #     p_Kanai,
        #     p_Kangiyanoor)
        
        # Drop_Location
        # Kanai = 0 (not in column)
        Drop_Location = request.form["Drop_Location"]
        if (Drop_Location == 'Kandamangalam'):
            d_Kandamangalam = 1
            d_Valavanur = 0
            d_Villupuram = 0
            d_Kilayanur = 0
            d_Nemili = 0
            
        elif (Drop_Location == 'Valavanur'):
            d_Kandamangalam = 0
            d_Valavanur = 1
            d_Villupuram = 0
            d_Kilayanur = 0
            d_Nemili = 0
            
        elif (Drop_Location == 'Villupuram'):
            d_Kandamangalam = 0
            d_Valavanur = 0
            d_Villupuram = 1
            d_Kilayanur = 0
            d_Nemili = 0
            
        elif (Drop_Location == 'Kilayanur'):
            d_Kandamangalam = 0
            d_Valavanur = 0
            d_Villupuram = 0
            d_Kilayanur = 1
            d_Nemili = 0
            
        elif (Drop_Location == 'Nemili'):
            d_Kandamangalam = 0
            d_Valavanur = 0
            d_Villupuram = 0
            d_Kilayanur = 0
            d_Nemili = 1
            
        else:
            d_Kandamangalam = 0
            d_Valavanur = 0
            d_Villupuram = 0
            d_Kilayanur = 0
            d_Nemili = 0
            
        # print(
        #     d_Kandamangalam,
        #     d_Valavanur,
        #     d_Villupuram,
        #     d_Kilayanur,
        #     d_Nemili
        # )
        #   ['Total_weight',
        #    'pickup_date_Journey_day','pickup_date_Journey_month',
        #    'Vehicle_Type_Tata_Ape','Vehicle_Type_Tata_Ace','Vehicle_Type_Ashok_Leyland','Vehicle_Type_Tata_407',
        #    'Pickup_Loocation_Agaram_Chithamoor','Pickup_Loocation_Kalpattu','Pickup_Loocation_Kanai','Pickup_Loocation_Kangiyanoor',
        #    'Drop_Location_Kandamangalam','Drop_Location_Valavanur','Drop_Location_Villupuram','Drop_Location_Kilayanur','Drop_Location_Nemili']
        
           
        prediction=model.predict([[
            Pickup_Location,
            Drop_Location,
            Vehicle_Type
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Consignment price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
        
        
            