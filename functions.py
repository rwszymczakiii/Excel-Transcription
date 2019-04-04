# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:19:30 2019

@author: rszymczak
"""
   
# this calculates the average from a list of values
def avg(alist):
    total = 0
    #total starts as 0
    for e in alist:
    # e will represent each value in the list
        total += e
        # each value in the list will be added to 0
    return total/len(alist)
    # the total is divided by the length of the list





# calculates the percent of one value from the total of two values for a given sheet
# This will only be used inside other functions 
    # the sheet must already be connected to an excel file as MNC is on line 32
def pcnt(sheet, r1, c1, r2, c2):
    # (value1 / value1 + value2) * 100 
    return (
        sheet.iloc[r1][c1] 
        / (sheet.iloc[r1][c1] 
        + sheet.iloc[r2][c2]) 
        * 100
        )
    # can calculate percent MNC from raw data




# calcuates standard deviation for a list of values the same way that excel's STDEV function does 
def stdev(alist):    
    mu = avg(alist)
    # mu is xbar 
    capsig = 0
    # this is the starting point for our sum (caipital sigma) of the numerator in the formula
    for e in alist:
        capsig += (e - mu) ** 2    
        
    return (capsig / (len(alist) - 1)) ** 0.5
     