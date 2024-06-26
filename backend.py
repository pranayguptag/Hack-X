from flask import Flask, render_template, request, send_from_directory
from crop_ml import predict_crop  # Assuming crop_ml.py has a predict function
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])  # Route for displaying the form
def index():
    # Display the form on GET request
    return render_template("index.html")

@app.route("/predict_scrollbar", methods=["POST"])  # Route for handling prediction request
def scrollbar():
    # Get user input on POST request
    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    temperature = float(request.form.get("temperature"))  # Handle potential missing key
    humidity = float(request.form.get("humidity"))  # Handle potential missing key
    ph = float(request.form.get("ph"))  # Handle potential missing key
    rainfall = float(request.form.get("rainfall"))  # Handle potential missing key

    # Call your machine learning model
    prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

    # Render the template with the prediction (optional, can redirect to success page)
    return render_template("prediction.html", scrollbar_prediction=prediction)


@app.route("/predict_dropdown", methods=["POST"])
def drop_down():
    # Sample location data (can be replaced with an actual data source)
    location_data = {
        "Delhi, India": {
            "nitrogen": 120.5,
            "phosphorus": 50.2,
            "potassium": 180.1,
            "temperature": 28.7,
            "humidity": 65.4,
            "ph": 7.2,
            "rainfall": 0.0  # Assuming no recent rainfall for this example
        },
        "Bangalore, India": {
            "nitrogen": 105.3,
            "phosphorus": 42.1,
            "potassium": 168.9,
            "temperature": 25.8,
            "humidity": 78.2,
            "ph": 6.8,
            "rainfall": 80  # Assuming some recent rainfall
        },
        # Add more locations as needed...
        "Mumbai, India" : { 
            "nitrogen": 26,
            "phosphorus": 27,
            "potassium": 10,
            "temperature": 28.06,
            "humidity": 92.9,
            "ph": 6.07,
            "rainfall": 114.13  # Assuming no recent rainfall for this example
        },
        "Kolkata, India" : { 
            "nitrogen": 90,
            "phosphorus": 42,
            "potassium": 43,
            "temperature": 20.87,
            "humidity": 82.2,
            "ph": 6.5,
            "rainfall": 150.93  # Assuming no recent rainfall for this example
        },
        "Chennai, India" : { 
            "nitrogen": 99,
            "phosphorus": 92,
            "potassium": 47,
            "temperature": 28.12,
            "humidity": 77.48,
            "ph": 6.3,
            "rainfall": 103.5  # Assuming no recent rainfall for this example
        },
        "Hyderabad, India" : { 
            "nitrogen": 55,
            "phosphorus": 35,
            "potassium": 50,
            "temperature": 30,
            "humidity": 70,
            "ph": 7,
            "rainfall": 70  # Assuming no recent rainfall for this example
        },
        "Pune, India" : { 
            "nitrogen": 50,
            "phosphorus": 30,
            "potassium": 45,
            "temperature": 26,
            "humidity": 65,
            "ph": 6.8,
            "rainfall": 80  # Assuming no recent rainfall for this example
        },
        "Ahmedabad, India" : { 
            "nitrogen": 127,
            "phosphorus": 37,
            "potassium": 18,
            "temperature": 24.8,
            "humidity": 76.3,
            "ph": 7.0,
            "rainfall": 91.9  # Assuming no recent rainfall for this example
        },
        "Jaipur, India" : { 
            "nitrogen": 13,
            "phosphorus": 67,
            "potassium": 18,
            "temperature": 29.3,
            "humidity": 45.9,
            "ph": 6.4,
            "rainfall": 165.4  # Assuming no recent rainfall for this example
        },
        "Lucknow, India" : { 
            "nitrogen": 55,
            "phosphorus": 30,
            "potassium": 55,
            "temperature": 23,
            "humidity": 65,
            "ph": 8,
            "rainfall": 110  # Assuming no recent rainfall for this example
        },
    }

    # Extract user-selected location from the request (if provided)
    selected_location = request.form.get("location")

    # Use default location data if none is selected
    #location_data_to_use = location_data.get("Bangalore, India")  # Default location
    if selected_location and selected_location in location_data:
        location_data_to_use = location_data[selected_location]

    # Extract crop data from the location data
    nitrogen = location_data_to_use["nitrogen"]
    phosphorus = location_data_to_use["phosphorus"]
    potassium = location_data_to_use["potassium"]
    temperature = location_data_to_use.get("temperature")
    humidity = location_data_to_use.get("humidity")
    ph = location_data_to_use.get("ph")
    rainfall = location_data_to_use.get("rainfall")

    # Call your machine learning model
    prediction = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

    # Render the template with the prediction (optional, can redirect to success page)
    return render_template("prediction.html", dropdown_prediction=prediction)

@app.route('/loan')
def loan():
    return render_template('loan.html')

@app.route('/show_form')
def show_form():
    return render_template('forms.html')

@app.route('/prediction')
def search():
    return render_template('prediction.html')

@app.route('/ads.txt')
def ads_txt():
    # Adjust the path if your ads.txt is located elsewhere
    return send_from_directory(app.static_folder, 'ads.txt')

@app.route('/kisan_seva_logo')
def website_logo():
    # Providing the correct path to the 'index' folder inside the 'static' folder
    directory_path = os.path.join(app.static_folder, 'index')
    return send_from_directory(directory_path, 'kisan_seva_logo_full.png')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

if __name__ == "__main__":
    app.run(debug=True)