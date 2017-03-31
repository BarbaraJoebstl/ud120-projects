#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#clf = SVC(kernel="linear")
#the accuracy gets worse if we use only 1% of the features with the more complex
#rbf kernel
clf = SVC(kernel="rbf", C=10000)
#c=1: accuracy: 0.616040955631
#c=10: accuracy: 0.616040955631
#c=100: accuracy: 0.616040955631
#c=1000: accuracy: 0.821387940842
#c=10000: accuracy: 0.892491467577

#These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data. You can leave all other code unchanged. 
#Only 1% of the features, but over 88% the performance (accurcy)
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

acc = accuracy_score(pred, labels_test)
print "accuracy", acc


answer=pred[10]
print "10", answer
answer=pred[26]
print "26", answer
answer=pred[50]
print "50", answer

chris_class = 0;
for chris in pred:
    if chris == 1:
        chris_class += 1

print "emails for chris", chris_class
#########################################################


