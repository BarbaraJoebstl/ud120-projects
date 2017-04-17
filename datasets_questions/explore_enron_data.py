#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

data_points = len(enron_data)
print 'datapoints:', data_points

no_of_features = len(enron_data[enron_data.keys()[0]])  
print 'number of features:', no_of_features

# count number of persons of interest
count = 0
for key in enron_data:
    if enron_data[key]['poi'] is True:
        count += 1

print 'number of persons of interest:', count

# What is the total value of the stock belonging to James Prentice?
james = enron_data["PRENTICE JAMES"]["total_stock_value"]
print 'James Prentice stock', james

# How many email messages do we have from Wesley Colwell to persons of interest?
wesley_emails = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print 'wesleys emails from', wesley_emails

# What s the value of stock options exercised by Jeffrey K Skilling
jeffrey = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print 'jeffreys stock options exersiced', jeffrey

jeffreys_money = enron_data["SKILLING JEFFREY K"]["total_payments"]
print 'jeffreys money', jeffreys_money

fastows_money = enron_data["FASTOW ANDREW S"]["total_payments"]
print 'fastows money', fastows_money

lays_money = enron_data["LAY KENNETH L"]["total_payments"]
print 'lays money', lays_money

#print enron_data.values()

# count number of persons of quantified salary
count_q_salary = 0
for key in enron_data:
    if enron_data[key]['salary'] != 'NaN':
        count_q_salary += 1

print 'number of persons with quantified salary:', count_q_salary

# count number of persons with email
count_email = 0
for key in enron_data:
    if enron_data[key]['email_address'] != 'NaN':
        count_email += 1

print 'number of persons with email:', count_email

# count number of persons of quantified salary
count_q_salary_nan = 0
for key in enron_data:
    if enron_data[key]['salary'] == 'NaN':
        count_q_salary_nan += 1

print 'number of persons with none quantified salary :', count_q_salary_nan

percentage = ((count_q_salary+count_q_salary_nan)/100.)*count_q_salary_nan
print percentage, '% don t have a quantified salary'

length = len(enron_data)
print 'Length of Dataset', len(enron_data)

#count total payments nan
count_total_payments_nan = 0
for key in enron_data:
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True:
        count_total_payments_nan += 1

print 'number of POIs with NaN Total Payments :', count_total_payments_nan

percentage_total_payments = ((length / 100.) * count_total_payments_nan)
print percentage_total_payments, '% of POIs don t have NaN for total payments'

#count pois
count_pois = 0
for key in enron_data:
    if enron_data[key]['poi'] == True:
        count_pois += 1

print 'number of POIs:', count_pois

#remove the spreadsheet error...
enron_data.pop("TOTAL", 0)

#max and min of exercised stock options

max_exercised_stock_options = float("-inf")
min_exercised_stock_options = float("inf")

for k, v in enron_data.iteritems():
    if v["exercised_stock_options"] != "NaN":
        if v["exercised_stock_options"] > max_exercised_stock_options:
            max_exercised_stock_options = v["exercised_stock_options"]
        if v["exercised_stock_options"] < min_exercised_stock_options:
            min_exercised_stock_options = v["exercised_stock_options"]

print 'MAX exercised stock options:', max_exercised_stock_options
print 'MIN exercised stock options:', min_exercised_stock_options

max_salary = float("-inf")
min_salary = float("inf")

for k, v in enron_data.iteritems():
    if v["salary"] != "NaN":
        if v["salary"] > max_salary:
            max_salary = v["salary"]
        if v["salary"] < min_salary:
            min_salary = v["salary"]

print 'MAX salary:', max_salary
print 'MIN salary:', min_salary

#MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
import numpy

scaler = MinMaxScaler()
salary_scaled_array = numpy.array([[min_salary], [200000.], [max_salary]])

rescaled_salary = scaler.fit_transform(salary_scaled_array)

print 'scaled salary for 200 000', rescaled_salary

stock_options_scaled_array = numpy.array([[min_exercised_stock_options], [1000000.], [max_exercised_stock_options]])
rescaled_stock_options = scaler.fit_transform(stock_options_scaled_array)

print 'scaled stock options for 1m', rescaled_stock_options
