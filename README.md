# api_test
Design -

I will be using python 3.9 to test the api. I am using the below libraries and their version in order to achieve the test framework -
1. requests 2.25.0 - This python library is being used to work with api requests in python.
2. pytest 6.1.2 - This library is a python testing framework using assert statements and can be run in batch mode from command line 

You can use the requirements.txt file in the package to install these libraries using pip 
pip install -r requirements.txt 

Test cases are as below -
1. Test the http response
2. Test whether the response is taking less than a second to come back
3. Test whether we are getting the latest hourly updates
4. Test whether the values on temperatures are not empty 	

Sample test run output -
Please install the python libraries pytest and requests before running these tests
To run the tests, run the following command from the directory where the api_test.py file is saved
pytest -v api_test.py
