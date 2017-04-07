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