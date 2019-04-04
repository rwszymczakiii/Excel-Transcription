# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:10:38 2019

@author: rszymczak
"""

import os
os.chdir('c:/users/rszymczak/desktop')

import pandas as pd


chsc = pd.read_excel('HDB.xlsx', 'CHO-K1,HC,SUMBERGED,CINT', header=None)
writer = pd.ExcelWriter('HDB format test.xlsx', engine='xlsxwriter') 
chsc.to_excel(writer, 'CHO-K1,HC,SUMBERGED,CINT', header=None, index=None)


HDB = writer.book
chsc = writer.sheets['CHO-K1,HC,SUMBERGED,CINT']

                             
ID_format = HDB.add_format(
        {'align': 'center', 
         'valign': 'vcenter',
         'text_wrap':True}
        )

data_format = HDB.add_format(
    {'num_format':'#,##0.00',
     'align': 'center',
     'valign': 'vcenter',
     'text_wrap':True}
    )


chsc.set_zoom(50)

chsc.set_column('A:C', 15, ID_format)
chsc.set_column('D:AA', 12, data_format)
chsc.set_column('AB:AG', 12, ID_format)

#chsc.merge_range('A3:C3', '')
#chsc.merge_range('A4:C4', '')
#chsc.merge_range('A5:C5', '')
#chsc.merge_range('D2:F2', '')
#chsc.merge_range('D3:F3', '')
#chsc.merge_range('D4:F4', '')
#chsc.merge_range('G1:R1', '')
#chsc.merge_range('G2:I2', '')
#chsc.merge_range('G3:I3', '')
#chsc.merge_range('G4:I4', '')
#chsc.merge_range('J2:J2', '')
#chsc.merge_range('J3:L3', '')
#chsc.merge_range('J4:L4', '')
#chsc.merge_range('M2:O2', '')
#chsc.merge_range('M3:O3', '')
#chsc.merge_range('M4:I4', '')
#chsc.merge_range('P2:R2', '')
#chsc.merge_range('P3:R3', '')
#chsc.merge_range('M4:I4', '')


writer.save() 