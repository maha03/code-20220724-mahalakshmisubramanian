''' This python script is to calculate BMI and evaluate the category and health risk status of an individual. The input
    from users are received through the .json file - input_data_raw.json. The attributes received from the user are Gender,
    Height in cm and Weight in Kg. Using these inputs, BMI , BMI category and health risk is calculated for each user.
    These calculated attributes along with the input attributes are written to an output .json file named as
    output_data_file.json. Error handling code is written inside the main().'''


import json
import numbers
import sys

''' The BMICalculator class accepts Height in cm, Weight in Kg as parameters. The bmi_category_health_risk_calculator
    method calculates the three attributes BMI , BMI category, health risk and returns them in a single dictionary 
    when it's called'''

class BMICalculator:
    #Constructor for BMICalculator
    def __init__(self, height_in_cm, weight_in_kg):
        self.height_in_cm=height_in_cm
        self.weight_in_kg=weight_in_kg

    #Method to calculate output attributes and return a dictionary
    def bmi_category_health_risk_calculator(self):
        body_mass_index = round(((self.weight_in_kg) / ((self.height_in_cm / 100) ** 2)), 1)
        bmi_category_health_risk = dict()
        if body_mass_index <= 18.4:
            bmi_category = "Underweight"
            health_risk = "Malnutrition risk"
        elif 18.5 <= body_mass_index <= 24.9:
            bmi_category = "Normal weight"
            health_risk = "Low risk"
        elif 25 <= body_mass_index <= 29.9:
            bmi_category = "Overweight"
            health_risk = "Enhanced risk"
        elif 30 <= body_mass_index <= 34.9:
            bmi_category = "Moderately obese"
            health_risk = "Medium risk"
        elif 35 <= body_mass_index <= 39.9:
            bmi_category = "Severely obese"
            health_risk = "High risk"
        else:
            bmi_category = "Very severely obese"
            health_risk = "Very high risk"
        bmi_category_health_risk['body_mass_index']= body_mass_index
        bmi_category_health_risk['bmi_category'] = bmi_category
        bmi_category_health_risk['health_risk'] = health_risk
        return bmi_category_health_risk

''' The main() function reads inputs from the input file, handles error in file and user records. Code to create object 
    and call methods are written here '''
def main():
    #variable to collect output data for user inputs in the input file
    output_data = []
    try:
        #Checks for error in file format
        with open("input_data_raw.json", 'r') as input_json_file:
            input_data = json.loads(input_json_file.read())
            user_no = 1
            for user in input_data:
                '''Checks for error in user data. Gender value is assumed to be a drop list in front end with only binary 
                   values. If there's an invalud value in a user data, file processing is continued for other user data'''
                try:
                    if user['HeightCm'] is None or not isinstance(user['HeightCm'], numbers.Number) or user['HeightCm'] < 0:
                        raise ValueError
                    if user['WeightKg'] is None or not isinstance(user['WeightKg'], numbers.Number) or user['WeightKg'] < 0:
                        raise ValueError
                except ValueError:
                    print(f'Invalid input for user {user_no}. Results for other users are in the output_data_file.json')
                    user_no+=1
                    continue
                #renaming the key values in user data to Python standards
                user['height_in_cm'] = user.pop('HeightCm')
                user['weight_in_kg'] = user.pop('WeightKg')
                #instantiating BMICalculator
                BMICalculator_object = BMICalculator(user['height_in_cm'], user['weight_in_kg'])
                #updating user data with 3 calculated attributes from the bmi_category_health_risk_calculator method
                user.update(BMICalculator_object.bmi_category_health_risk_calculator())
                #appending the user data with 6 key-value pairs to output variable
                output_data += [user]
                user_no+=1
    except:
        print("Invalid input file")
        sys.exit(1)

    #Writing the output variable to output .json file
    with open('output_data_file.json', 'w') as outfile:
        outfile.truncate()
        json.dump(output_data, outfile, indent=4)
        outfile.close()

main()