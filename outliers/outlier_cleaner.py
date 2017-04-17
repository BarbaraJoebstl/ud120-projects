#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    #calculating the SSE(sum of squared errors)
    error = (net_worths - predictions)**2
    #stack array horizontally
    hstack = np.hstack((ages, net_worths, error))
    #print hstack
    list = hstack.tolist()
    #sort the list
    list = sorted(list,key=lambda x: x[2])
    #remove 10% of the outliers
    n=len(list)/10
    cleaned_data=list[0:-n]
    return cleaned_data    

