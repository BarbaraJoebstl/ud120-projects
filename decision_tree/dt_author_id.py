#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn import tree

#These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data. You can leave all other code unchanged. 
#Only 1% of the features, but over 88% the performance (accurcy)
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)

acc = clf.score(features_test, labels_test)
print "accuracy split40(percentile_10):", round(acc,3)

number_of_features = len(features_train[0])
print "number of features(percentile_10): ", number_of_features
#Percentile_10: 3785
#########################################################


