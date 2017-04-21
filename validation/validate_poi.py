#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!  

from sklearn import tree
from sklearn.svm import SVC

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

acc = clf.score(features, labels)
print "accuracy split", round(acc, 3)

from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    features, labels, test_size=0.3, random_state=42)

clf.fit(features_train, labels_train)
accurracy = clf.score(features_test, labels_test)

print 'Accuracy with Cross Validation:', accurracy

#count pois in testdata (pois will be labeld with 1.0)
count_pois = 0
for poi in labels_test:
    if poi == 1.0:
        count_pois += 1

print 'number of POIs in the test set:', count_pois

#number of people in the testset
count_people = len(labels_test)
print 'total number of people in the test set:', count_people

count_non_pois = count_people - count_pois
print 'number of none pois', count_non_pois
#accuracy
accuray_for_non_poi = float(count_non_pois/count_people)
print 'accuracy for non pois', accuray_for_non_poi

#count performanes

def count_true_positives(labels, labels_train):
    true_positives_ = 0
    for i in range(len(labels_train)): 
        if labels[i]==labels_train[i]=='1.0':
            true_positives_ += 1
    return true_positives_

true_positives = count_true_positives(labels, labels_train)
print 'number of true_positives in the test set:', true_positives

#precision_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

ps = precision_score(labels, labels, average=None)
print 'precision score', ps

rs = recall_score(labels, labels, average=None)
print 'recall score', rs

#exmple true positvies
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positives_2 = 0
for i in range(len(predictions)): 
    if true_labels[i]==predictions[i]== 1:
        true_positives_2 += 1
print 'number of true_positives_2 in the test set:', true_positives_2

true_negatives = 0
for i in range(len(predictions)): 
    if true_labels[i]==predictions[i]== 0:
        true_negatives += 1
print 'number of true_negatives in the test set:', true_negatives

false_positives = 0
for i in range(len(predictions)): 
    if true_labels[i]!= predictions[i] == 1:
        false_positives += 1
print 'number of false positives in the test set:', false_positives

false_negatives = 0
for i in range(len(predictions)): 
    if true_labels[i]!= predictions[i] == 0:
        false_negatives += 1
print 'number of false negatives in the test set:', false_negatives 

#precision
precision = float(true_positives/(true_positives+false_positives))
print precision


#recall
recall = float(true_positives/(true_positives+false_negatives))
print precision