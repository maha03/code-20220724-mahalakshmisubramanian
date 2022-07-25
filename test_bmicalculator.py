''' This Python script contains unit test cases for the bmi_calculator.py. '''
import unittest
from bmi_calculator import BMICalculator


class TestBMICalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        pass

    '''This code instantiates BMICalculator class in bmi_calculator.py.'''
    def setUp(self):
        self.user_1 = BMICalculator(147, 39.7)
        self.user_2 = BMICalculator(150, 41.7)
        self.user_3 = BMICalculator(152, 57.5)
        self.user_4 = BMICalculator(155, 60)
        self.user_5 = BMICalculator(157, 73.6)
        self.user_6 = BMICalculator(163, 79.6)
        self.user_7 = BMICalculator(165, 94.9)
        self.user_8 = BMICalculator(167.5, 98.3)
        self.user_9 = BMICalculator(172, 118)
        self.user_10 = BMICalculator(175, 122.5)
        self.user_11 = BMICalculator(177, 140)
        self.user_12 = BMICalculator(145, 37)
        self.user_13 = BMICalculator(151, 48.7)
        self.user_14 = BMICalculator(156, 65)
        self.user_15 = BMICalculator(164, 85)
        self.user_16 = BMICalculator(168, 105)
        self.user_17 = BMICalculator(175, 160)

    def tearDown(self):
        print('tearDown\n')

    ''' This block calls the bmi_category_health_risk_calculator method from BMICalculator class and validates the values
    it returns. There are a total of 17 different test data corresponding to boundary value analysis approach'''
    def test_bmi_category_health_risk_calculator(self):
        expected_output_1 = self.user_1.bmi_category_health_risk_calculator()
        actual_output_1 = {'body_mass_index': 18.4, 'bmi_category': 'Underweight', 'health_risk': 'Malnutrition risk'}
        self.assertDictEqual(expected_output_1, actual_output_1)

        expected_output_2 = self.user_2.bmi_category_health_risk_calculator()
        actual_output_2 = {'body_mass_index': 18.5, 'bmi_category': 'Normal weight', 'health_risk': 'Low risk'}
        self.assertDictEqual(expected_output_2, actual_output_2)

        expected_output_3 = self.user_3.bmi_category_health_risk_calculator()
        actual_output_3 = {'body_mass_index': 24.9, 'bmi_category': 'Normal weight', 'health_risk': 'Low risk'}
        self.assertDictEqual(expected_output_3, actual_output_3)

        expected_output_4 = self.user_4.bmi_category_health_risk_calculator()
        actual_output_4 = {'body_mass_index': 25, 'bmi_category': 'Overweight', 'health_risk': 'Enhanced risk'}
        self.assertDictEqual(expected_output_4, actual_output_4)

        expected_output_5 = self.user_5.bmi_category_health_risk_calculator()
        actual_output_5 = {'body_mass_index': 29.9, 'bmi_category': 'Overweight', 'health_risk': 'Enhanced risk'}
        self.assertDictEqual(expected_output_5, actual_output_5)

        expected_output_6 = self.user_6.bmi_category_health_risk_calculator()
        actual_output_6 = {'body_mass_index': 30, 'bmi_category': 'Moderately obese', 'health_risk': 'Medium risk'}
        self.assertDictEqual(expected_output_6, actual_output_6)

        expected_output_7 = self.user_7.bmi_category_health_risk_calculator()
        actual_output_7 = {'body_mass_index': 34.9, 'bmi_category': 'Moderately obese', 'health_risk': 'Medium risk'}
        self.assertDictEqual(expected_output_7, actual_output_7)

        expected_output_8 = self.user_8.bmi_category_health_risk_calculator()
        actual_output_8 = {'body_mass_index': 35, 'bmi_category': 'Severely obese', 'health_risk': 'High risk'}
        self.assertDictEqual(expected_output_8, actual_output_8)

        expected_output_9 = self.user_9.bmi_category_health_risk_calculator()
        actual_output_9 = {'body_mass_index': 39.9, 'bmi_category': 'Severely obese', 'health_risk': 'High risk'}
        self.assertDictEqual(expected_output_9, actual_output_9)

        expected_output_10 = self.user_10.bmi_category_health_risk_calculator()
        actual_output_10 = {'body_mass_index': 40, 'bmi_category': 'Very severely obese', 'health_risk': 'Very high risk'}
        self.assertDictEqual(expected_output_10, actual_output_10)

        expected_output_11 = self.user_11.bmi_category_health_risk_calculator()
        actual_output_11 = {'body_mass_index': 44.7, 'bmi_category': 'Very severely obese',
                            'health_risk': 'Very high risk'}
        self.assertDictEqual(expected_output_11, actual_output_11)

        expected_output_12 = self.user_12.bmi_category_health_risk_calculator()
        actual_output_12 = {'body_mass_index': 17.6, 'bmi_category': 'Underweight',
                            'health_risk': 'Malnutrition risk'}
        self.assertDictEqual(expected_output_12, actual_output_12)

        expected_output_13 = self.user_13.bmi_category_health_risk_calculator()
        actual_output_13 = {'body_mass_index': 21.4, 'bmi_category': 'Normal weight',
                            'health_risk': 'Low risk'}
        self.assertDictEqual(expected_output_13, actual_output_13)

        expected_output_14 = self.user_14.bmi_category_health_risk_calculator()
        actual_output_14 = {'body_mass_index': 26.7, 'bmi_category': 'Overweight',
                            'health_risk': 'Enhanced risk'}
        self.assertDictEqual(expected_output_14, actual_output_14)

        expected_output_15 = self.user_15.bmi_category_health_risk_calculator()
        actual_output_15 = {'body_mass_index': 31.6, 'bmi_category': 'Moderately obese',
                            'health_risk': 'Medium risk'}
        self.assertDictEqual(expected_output_15, actual_output_15)

        expected_output_16 = self.user_16.bmi_category_health_risk_calculator()
        actual_output_16 = {'body_mass_index': 37.2, 'bmi_category': 'Severely obese', 'health_risk': 'High risk'}
        self.assertDictEqual(expected_output_16, actual_output_16)

        expected_output_17 = self.user_17.bmi_category_health_risk_calculator()
        actual_output_17 = {'body_mass_index': 52.2, 'bmi_category': 'Very severely obese', 'health_risk':
                            'Very high risk'}
        self.assertDictEqual(expected_output_17, actual_output_17)


if __name__ == '__main__':
    unittest.main()
