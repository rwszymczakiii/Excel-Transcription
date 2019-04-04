# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:23:28 2019

@author: rszymczak
"""

import pandas as pd
import os
from xlrd import XLRDError





# to change path to user's desktop
while True:
    
    try:
    # asks user for work id:
        name = input('Enter your user ID: ')
        name = name.lower()
        # corrects for capitalization
        
        os.chdir(f'c:/users/{name}/desktop')
        desktop = f'c:/users/{name}/desktop'
        # changes the path that python uses to find files 
        # on the user's desktop        
        break
            
    except FileNotFoundError:
        print ('\nPlease try again.\nYour user ID is your first initial' 
               ' and last name.')                    


files = os.listdir(path = desktop)        
files = dict(enumerate(files))
# generates a dictionary that includes all files on the user's desktop





while True:
    print(f'\nHere are the files on your DESKTOP:\n{files}')
    
    try:      
        
        assay = int(input('Please provide the number that corresponds' 
                          ' with your ASSAY WORKSHEET: '))
        
        if assay >= len(files):
            print('\nThe number you have entered is not valid.' 
                  ' Please try again.')
            # prevents assay from being defined as None
            
        else:
            assay = files.get(assay)
            
            
            check = input(f'\nYou selected {assay} as your'
                          ' ASSAY WORKSHEET.' 
                          ' Is this correct? y/n ')
            check = check.upper()

            if check == 'Y':        
                break
                # loop only ends when the user has confirmed their input  
            
            else: 
                print("\nlet's try again")  
        
    except ValueError:
        print("\nInput not recognized.")
        # value error occurs for non-integer inputs 





sheets = pd.ExcelFile(assay).sheet_names  
sheets = dict(enumerate(sheets))
# creates a dictionary of all sheets so that the user only needs 
# to input a number

# dictionaries also make the code faster




try:
    MNC = pd.read_excel(assay, sheet_name = '%MNC (Manual)', header = None)

except XLRDError:
    
    while True:
        
        print ('\nHere are the sheets found in your ASSAY WORKSHEET:'
               f'\n{sheets} ')        
        
        try:
        
            num = int(input('\nPlease provide the number that corresponds' 
                            ' with your MNC SCORE sheet: '))
            
            if num >= len(sheets):
                print('\nThe number you have entered is not valid.'
                      ' Please try again.')
                continue
            
            MNC = sheets.get(num)
            
            check = input(f'\nYou selected {MNC} as your MNC SCORE sheet.'
                          ' Is this correct? y/n ')
            check = check.upper()
        
            if check == 'Y':     
                
                MNC = pd.read_excel(
                    assay, 
                    sheet_name = MNC, 
                    header = None
                    )
                
                break
                    
            else:        
                print("let's try again.")
                        
        except ValueError:
            print("\nInput not recognized.")
       
            
            
        
            
try:
    fixtox = pd.read_excel(
        assay, 
        sheet_name = 'Fixation and Toxicity', 
        header = None
        )
         
except XLRDError:
        
    while True:
       
        print ('\nHere are the sheets found in your ASSAY WORKSHEET:'
               f'\n{sheets} ')       
        
        try:
        
            num = int(input('\nPlease provide the number that corresponds'
                            ' with your FIXATION AND TOXICITY sheet: '))

            if num >= len(sheets):
                print('\nThe number you have entered is not valid.\
                      Please try again.')
                continue
            
            fixtox = sheets.get(num)        
            
            check = input(f'\nYou selected {fixtox} as your'
                          ' FIXATION AND TOXICITY sheet.'
                          ' Is this correct? y/n ')
            check = check.upper()
        
            if check == 'Y':        
                pd.ExcelFile(assay)
                fixtox = pd.read_excel(
                    assay, 
                    sheet_name = fixtox, 
                    header = None
                    )
                
                break
                    
            else:        
                print("\nlet's try again.")
               
        except ValueError:
            print("\nInput not recognized.")  
            



    
try:
    sampleID = pd.read_excel(assay, sheet_name = 'Sample ID HC', 
                             header = None)
         
except XLRDError:
        
    while True:
       
        print ('\nHere are the sheets found in your ASSAY WORKSHEET:'
               f'\n{sheets}')        
    
        try:
        
            num = int(input('\nPlease provide the number that corresponds'
                            ' with your SAMPLE ID sheet: '))
           
            if num >= len(sheets):
                print('\nThe number you have entered is not valid.' 
                      ' Please try again.')
                continue
            
            sampleID = sheets.get(num)    

            check = input(f'\nYou selected {sampleID} as your SAMPLE ID'
                          ' sheet. Is this correct? y/n ')
            check = check.upper()
        
            if check == 'Y':        
                pd.ExcelFile(assay)
                sampleID = pd.read_excel(
                    assay, 
                    sheet_name = sampleID, 
                    header = None
                    )
                
                break
                    
            else:        
                print("\nlet's try again")
                
        except ValueError:
            print("\nInput not recognized") 

    
    

            
try:
    HDB = pd.read_excel('HDB, ALL.xlsx')
    HDB = 'HDB, ALL.xls'
    
except FileNotFoundError:
    try:
        HDB = pd.read_excel('HDB, ALL.xls')
        HDB = 'HDB, ALL.xlsx'

# HDB will be added to the user's desktop from the ECM. 
# Therefore, the currently used HDB should have the same name 
# and does not require user input
    # but just in case:
        
    except FileNotFoundError:      
        
        while True: 
        # to define HDB
            
            print('\n\nNow we need the HISTORICAL DATABASE.'
                  f'\nHere are the files on your DESKTOP:\n{files}') 

            try:                     
                num = int(input('\nPlease provide the number that'
                                ' corresponds with your'
                                ' HISTORICAL DATABASE file: '))
                
                if num >= len(files):
                    print('\nThe number you have entered is not valid.' 
                          ' Please try again.')
                    
                else:
                    HDB = files.get(num)                   
                    
                    check = input(f'\nYou selected {HDB} as your'
                                  ' HISTORICAL DATABASE file.' 
                                  ' Is this correct? y/n ')
                    check = check.upper()
    
                    if check == 'Y':        
                        break
                    
                    else: 
                        print("\nlet's try again")
                        
            except ValueError:
                print("\nInput not recognized.")
 
 
 

       
sheets = pd.ExcelFile(HDB).sheet_names  
sheets = dict(enumerate(sheets))
 
print('\nHere are the available sheets in your HISTORICAL DATABASE:'
      f'\n{sheets}')
 
 
 
 
  
while True:
     
    try:       
        num = int(input('\nPlease provide the number that corresponds'
                        ' with your SMOKE AND CELL CULTURE CONDITIONS: '))
        
        if num >= len(sheets):
            print('\nThe number you have entered is not valid.'
                  ' Please try again.')
        
        else:        
            HDB_sheet = sheets.get(num)

            check = input(f'\nYou selected {HDB_sheet} as your'
                          ' SMOKE AND CELL CULTURE CONDITIONS.'
                          ' Is this correct? y/n ')
            check = check.upper()

            if check == 'Y':        
                HDB_sheet_df = pd.read_excel(
                        HDB, 
                        sheet_name = HDB_sheet, 
                        header = None
                        )                
                break
            
            else: 
                print("\nlet's try again")            

    except ValueError:
        print('\nInput not recognized.')
                 