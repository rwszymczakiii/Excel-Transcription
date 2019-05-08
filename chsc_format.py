# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:02:59 2019

@author: rszymczak
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:10:38 2019

@author: rszymczak
"""


# =============================================================================
# imports
# =============================================================================
import os
import pandas as pd
import pandas.io.formats.excel
#import datetime

# =============================================================================
# to extract the data from a file
# =============================================================================
os.chdir('c:/users/rszymczak/desktop')

chsc_read = pd.read_excel('HDB2.xlsx', 'CHO-K1,HC,SUMBERGED,CINT')

## =============================================================================
## formating the new sheet
## =============================================================================
pandas.io.formats.excel.header_style = None

chsc_writer = pd.ExcelWriter('HDB format test.xlsx', engine='xlsxwriter') 

chsc_read.to_excel(chsc_writer, 'CHO-K1,HC,SUMBERGED,CINT', header=None)

HDB_workbook = chsc_writer.book
chsc_worksheet = chsc_writer.sheets['CHO-K1,HC,SUMBERGED,CINT']
                        
ID_format = HDB_workbook.add_format(
        {'align': 'center', 
         'valign': 'vcenter',
         'text_wrap':True}
        )

data_format = HDB_workbook.add_format(
    {'num_format':'#,##0.00',
     'align': 'center',
     'valign': 'vcenter',
     'text_wrap':True}
    )



chsc_worksheet.set_zoom(50)

project = 'project#'
chsc_worksheet.set_header(f'&LProject:\nother text')

chsc_worksheet.set_column('A:C', 15, ID_format)
chsc_worksheet.set_column('D:AA', 12, data_format)
chsc_worksheet.set_column('AB:AG', 12, ID_format)

#assay_startdate_col =chsc_read.loc[]
#chsc_worksheet.write_datetime('AE', datetime.date('%d%b%y'), ID_format)

chsc_worksheet.merge_range('D1:F1', '')
chsc_worksheet.merge_range('F2:F3', '')
#chsc_worksheet.merge_range('D3:F3', '')
chsc_worksheet.merge_range('G1:I1', '')
chsc_worksheet.merge_range('G2:I2', '')
chsc_worksheet.merge_range('G3:I3', '')
chsc_worksheet.merge_range('J1:L1', '')
chsc_worksheet.merge_range('J2:L2', '')
chsc_worksheet.merge_range('J3:L3', '')
chsc_worksheet.merge_range('M1:O1', '')
chsc_worksheet.merge_range('M2:O2', '')
chsc_worksheet.merge_range('M3:O3', '')
chsc_worksheet.merge_range('P1:R1', '')
chsc_worksheet.merge_range('P2:R2', '')
chsc_worksheet.merge_range('P3:R3', '')
chsc_worksheet.merge_range('S1:U1', '')
chsc_worksheet.merge_range('S2:U2', '')
chsc_worksheet.merge_range('S3:U3', '')
chsc_worksheet.merge_range('V1:X1', '')
chsc_worksheet.merge_range('V2:X2', '')
chsc_worksheet.merge_range('V3:X3', '')
chsc_worksheet.merge_range('Y1:AA1', '')
chsc_worksheet.merge_range('Y2:AA2', '')
chsc_worksheet.merge_range('Y3:AA3', '')



#for f in range(len(chsc_read.index)):
#    i=0
#    f=1
#    if chsc_read.loc[3][f] != None:
#        i+=f
#        chsc_worksheet.merge_range(3,0,3,f,'')
        




chsc_writer.save() 