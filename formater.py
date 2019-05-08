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
from os import chdir
import pandas as pd
import pandas.io.formats.excel
from calculations import HDB_sheet_df
from user_input import name
from user_input import HDB
from user_input import HDB_sheet
#import datetime
def formater():
    # =============================================================================
    # open the edited sheet
    # =============================================================================
    chdir(f'c:/users/{name}/desktop')
#    chsc_read = pd.read_excel('HDB2.xlsx', 'CHO-K1,HC,SUMBERGED,CINT')
    
    
    # these will be used to create the new HDB sheet at the end of the program
    # excelwriter will overwrite one of these with the edited dataframe with 
    # to excel     
    aoac = pd.read_excel(HDB, 'A549,OECD,ALI,CINT', header=None)
    aosc = pd.read_excel(HDB, 'A549,OECD,SUBMERGED,CINT', header=None)
    tosi = pd.read_excel(HDB, 'TK6,OECD,SUBMERGED,ISO', header=None)
    voac = pd.read_excel(HDB, 'V79,OECD,ALI,CINT', header=None)
    voai = pd.read_excel(HDB, 'V79,OECD,ALI,ISO', header=None)
    vosi = pd.read_excel(HDB, 'V79,OECD,SUMBERGED,ISO', header=None)
    chsc = pd.read_excel(HDB, 'CHO-K1,HC,SUMBERGED,CINT', header=None)
    chsi = pd.read_excel(HDB, 'CHO-K1,HC,SUMBERGED,ISO',  header=None)
    
   
    
    ## =============================================================================
    ## formating the new sheet
    ## =============================================================================
    pandas.io.formats.excel.header_style = None
    
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
    HDB_sheet_df.to_excel(writer, str(HDB_sheet), header=None)



    
    HDB_workbook = writer.book
    chsc_worksheet = writer.sheets['CHO-K1,HC,SUMBERGED,CINT']
                            
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
    
#    project = 'project#'
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
            
    
    
    
        # speed could be increased with if statement using the determined HDB_sheet
    # to not generate the unedited version

    
    writer.save()

    
    
    
    
    
    
    
    
    