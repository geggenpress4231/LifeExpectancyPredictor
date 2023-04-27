from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import pickle
from flask import jsonify
app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response




# Load the pre-trained model
model = pickle.load(open('predictor_model.pkl', 'rb'))
print(model.feature_names_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the HTML form
    country = request.form['country']
    year = int(request.form['year'])
    status = request.form['status']
    adult_mortality = float(request.form['adult_mortality'])
    infant_deaths = int(request.form['infant_deaths'])
    alcohol = float(request.form['alcohol'])
    percentage_expenditure = float(request.form['percentage_expenditure'])
    hepatitis_b = float(request.form['hepatitis_b'])
    measles = int(request.form['measles'])
    bmi = float(request.form['bmi'])
    under_five_deaths = int(request.form['under_five_deaths'])
    polio = float(request.form['polio'])
    total_expenditure = float(request.form['total_expenditure'])
    diphtheria = float(request.form['diphtheria'])
    hiv_aids = float(request.form['hiv_aids'])
    gdp = float(request.form['gdp'])
    population = int(request.form['population'])
    thinness_1_19_years = float(request.form['thinness_1_19_years'])
    thinness_5_9_years = float(request.form['thinness_5_9_years'])
    income_composition = float(request.form['income_composition'])
    schooling = float(request.form['schooling'])

    print(population)

    # Convert the input values to a pandas dataframe
    required_features = ['Country_Angola', 'Country_Central African Republic', 'Country_Chad', "Country_Côte d'Ivoire", 'Country_Lesotho', 'Country_Malawi', 'Country_Nigeria', 'Country_Zimbabwe','Status_Developed','Status_Developing','Year','Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio', 'Total Expenditure', 'Diphtheria', 'HIV/AIDS', 'GDP', 'Population', 'thinness  1-19 years', 'thinness 5-9 years', 'Income composition of resources', 'Schooling'] # list of all required feature names
    input_data = pd.DataFrame(columns=required_features) # create empty dataframe with required features
    for i in input_data.columns:
        if country==i:
            input_data.i=1
        else:
            input_data.i=0

# add values for existing features
         
# add values for existing features


    if(status=='Developed'):
        input_data.Status_Developed[0]=1
        input_data.Status_Developing[0]=0
    else:
        input_data.Status_Developed[0]=0
        input_data.Status_Developing[0]=1
            

    input_data.loc[0] = [0]*len(required_features)
    input_data['Year'][0] = year
    input_data['Adult Mortality'][0] = adult_mortality
    input_data['infant deaths'][0] = infant_deaths
    input_data['Alcohol'][0] = alcohol
    input_data['percentage expenditure'][0] = percentage_expenditure
    input_data['Hepatitis B'][0] = hepatitis_b
    input_data['Measles'][0] = measles
    input_data['BMI'][0] = bmi
    input_data['under-five deaths'][0] = under_five_deaths
    input_data['Polio'][0] = polio
    input_data['Total Expenditure'][0] = total_expenditure
    input_data['Diphtheria'][0] = diphtheria
    input_data['HIV/AIDS'][0] = hiv_aids
    input_data['GDP'][0] = gdp
    input_data['Population'][0] = population
    input_data['thinness  1-19 years'][0] = thinness_1_19_years
    input_data['thinness 5-9 years'][0] = thinness_5_9_years
    input_data['Income composition of resources'][0] = income_composition
    input_data['Schooling'][0] = schooling


    print(input_data.Alcohol)

    

    from sklearn.preprocessing import StandardScaler


    #Select the numerical columns
    num_cols = ['Year','Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles', 'BMI', 'under-five deaths', 'Polio', 'Total Expenditure', 'Diphtheria', 'HIV/AIDS', 'GDP', 'Population', 'thinness  1-19 years', 'thinness 5-9 years', 'Income composition of resources', 'Schooling']
    print(input_data[num_cols].columns)
#Create a StandardScaler object
    scaler = StandardScaler()

#Normalize the numerical columns
    input_data[num_cols] = scaler.fit_transform(input_data[num_cols])

    # Preprocess the input data
    # Your preprocessing code here...
    #add feature selection
    # Define the list of columns to keep
    cols_to_keep = ["Country_Angola", "Country_Central African Republic", "Country_Chad", "Country_Côte d'Ivoire", "Country_Lesotho","Country_Malawi", "Country_Nigeria", "Country_Zimbabwe", 'Status_Developed', 'Status_Developing', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 'BMI', 'under-five deaths', 'Polio', 'Diphtheria', 'HIV/AIDS', 'thinness  1-19 years', 'Income composition of resources', 'Schooling']

# Drop the columns that are not in the list
    input_data = input_data.loc[:, cols_to_keep]

    print(input_data.columns)
    # Make the prediction using the pre-trained model
    prediction = model.predict(input_data)

    # Return the prediction to the HTML page
    #return render_template('home.html', prediction_text='Predicted Life Expectancy: {:.2f}'.format(prediction[0]))
    response={"prediction":prediction[0]}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
