# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:55:30 2019

@author: rszymczak
"""

import pandas as pd
from user_input import HDB
from user_input import HDB_sheet
from calculations import HDB_sheet_df


print('\nOne moment please.')


# these will be used to create the new HDB sheet at the end of the program
    # excelwriter will overwrite one of these with the edited dataframe with to_excel     
aoac = pd.read_excel(HDB, 'A549,OECD,ALI,CINT', header=None)
aosc = pd.read_excel(HDB, 'A549,OECD,SUBMERGED,CINT', header=None)
tosi = pd.read_excel(HDB, 'TK6,OECD,SUBMERGED,ISO', header=None)
voac = pd.read_excel(HDB, 'V79,OECD,ALI,CINT', header=None)
voai = pd.read_excel(HDB, 'V79,OECD,ALI,ISO', header = None)
vosi = pd.read_excel(HDB, 'V79,OECD,SUMBERGED,ISO', header=None)
chsc = pd.read_excel(HDB, 'CHO-K1,HC,SUMBERGED,CINT', header=None)
chsi = pd.read_excel(HDB, 'CHO-K1,HC,SUMBERGED,ISO',  header=None)




writer = pd.ExcelWriter('Excelwriter test.xlsx', engine='xlsxwriter')    

aoac.to_excel(writer, 'A549,OECD,ALI,CINT',  
              header=None, index=None)    
aosc.to_excel(writer, 'A549,OECD,SUBMERGED,CINT', 
              header=None, index=None)
tosi.to_excel(writer, 'TK6,OECD,SUBMERGED,ISO', 
              header=None, index=None)
voac.to_excel(writer, 'V79,OECD,ALI,CINT', 
              header=None, index=None)
voai.to_excel(writer, 'V79,OECD,ALI,ISO', 
              header=None, index=None)
vosi.to_excel(writer, 'V79,OECD,SUMBERGED,ISO', 
              header=None, index=None)
chsc.to_excel(writer, 'CHO-K1,HC,SUMBERGED,CINT', 
              header=None, index=None)
chsi.to_excel(writer, 'CHO-K1,HC,SUMBERGED,ISO', 
              header=None, index=None)
HDB_sheet_df.to_excel(writer, str(HDB_sheet), header=None, index=None)
    
writer.save()

print("\nAll done. \n\nYou're welcome.")