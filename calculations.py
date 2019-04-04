# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:07:02 2019

@author: rszymczak
"""
### currently only works for HC


import functions as fun
import pandas as pd
from user_input import MNC
from user_input import fixtox
from user_input import sampleID as ID
from user_input import assay
from user_input import HDB_sheet_df





# to find the next empty row

cell = 5

while cell < 996:
    
    if pd.isnull(HDB_sheet_df[0][cell]) == False:
        
        cell += 1
        
        
    elif pd.isnull(HDB_sheet_df[0][cell]) == True:
        
        HDB_sheet_df.at[cell,1] = ID.at[13,0]
        HDB_sheet_df.at[cell,2] = assay
        HDB_sheet_df.at[cell, 30] = ID.at[13,3]
        
        break
    
    # cell can now be used for all future entries:    





# =============================================================================
# -S9 growth flask
# =============================================================================

ms9_gf_cytox = 0
    # growth flask cytotoxicity will always be 0
   
ms9_gf_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 275, 5, 275, 3), 
     fun.pcnt(MNC, 280, 5, 280, 3)]
    )
    # calculates %MNC    
ms9_gf_stdev = fun.stdev(
    [fun.pcnt(MNC, 275, 5, 275, 3), 
     fun.pcnt(MNC, 280, 5, 280, 3)]
    )      
    # standard deviation of percent MNC
    
ms9_gf_foldinc = 1
    # growth flask mean fold increase will always be 1





HDB_sheet_df.at[cell, 3] = ms9_gf_cytox
HDB_sheet_df.at[cell, 4] = ms9_gf_avgpcntMNC
HDB_sheet_df.at[cell, 5] = ms9_gf_stdev





# =============================================================================
# -S9 Vehicle Control
# =============================================================================

ms9_vc_cytox = 0
    # always 0 for VCs

ms9_vc_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 25, 5, 25, 3), 
     fun.pcnt(MNC, 30, 5, 30, 3)]
    )
    # calculates %MNC    
ms9_vc_stdev = fun.stdev(
        [fun.pcnt(MNC, 25, 5, 25, 3), 
         fun.pcnt(MNC, 30, 5, 30, 3)]
        )     
    # standard deviation of percent MNC
    




HDB_sheet_df.at[cell, 6] = ms9_vc_cytox
HDB_sheet_df.at[cell, 7] = ms9_vc_avgpcntMNC
HDB_sheet_df.at[cell, 8] = ms9_vc_stdev





# =============================================================================
# -S9 Positive Control  
# =============================================================================


ms9_pc_avgcytox = fun.avg(
    [100 - (((fixtox.at[3,8] * fixtox.at[15,2]) 
     / fixtox.at[10,8]) * 100),
     100 - (((fixtox.at[3,8] * fixtox.at[20,2]) 
     / fixtox.at[10,8]) * 100)]
    )

ms9_pc_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 5, 5, 5, 3), 
     fun.pcnt(MNC, 10, 5, 10, 3)]
    )
    # calculates %MNC    
ms9_pc_stdev = fun.stdev(
    [fun.pcnt(MNC, 5, 5, 5, 3), 
     fun.pcnt(MNC, 10, 5, 10, 3)]
    )     
    # standard deviation of percent MNC
    
ms9_pc_foldinc = ms9_pc_avgpcntMNC / ms9_vc_avgpcntMNC
    # from mean fold increase columnn on short term data summary sheet of assay            





HDB_sheet_df.at[cell, 12] = ms9_pc_avgcytox
HDB_sheet_df.at[cell, 13] = ms9_pc_avgpcntMNC
HDB_sheet_df.at[cell, 14] = ms9_pc_stdev





# =============================================================================
# -S9 Lab Reference
# =============================================================================

ms9_ref_avgcytox = fun.avg(
    [100 - (((fixtox.at[3,8] * fixtox.at[25,2]) 
     / fixtox.at[10,8]) * 100),
     100 - (((fixtox.at[3,8] * fixtox.at[30,2]) 
     / fixtox.at[10,8]) * 100)]
    )

ms9_ref_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 15, 5, 15, 3), 
     fun.pcnt(MNC, 20, 5, 20, 3)]
    )
    # calculates %MNC    
ms9_ref_stdev = fun.stdev(
    [fun.pcnt(MNC, 15, 5, 15, 3), 
     fun.pcnt(MNC, 20, 5, 20, 3)]
    )     
    # standard deviation of percent MNC
    




HDB_sheet_df.at[cell, 15] = ms9_ref_avgcytox
HDB_sheet_df.at[cell, 16] = ms9_ref_avgpcntMNC
HDB_sheet_df.at[cell, 17] = ms9_ref_stdev





# =============================================================================
# +S9 Vehicle Control
# =============================================================================

ps9_vc_cytox = 0
    # always 0 for VCs

ps9_vc_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 115, 5, 115, 3), 
     fun.pcnt(MNC, 120, 5, 120, 3)]
    )
    # calculates %MNC    
ps9_vc_stdev = fun.stdev(
    [fun.pcnt(MNC, 115, 5, 115, 3), 
     fun.pcnt(MNC, 120, 5, 120, 3)]
    )     
    # standard deviation of percent MNC
    




HDB_sheet_df.at[cell, 18] = ps9_vc_cytox
HDB_sheet_df.at[cell, 19] = ps9_vc_avgpcntMNC
HDB_sheet_df.at[cell, 20] = ps9_vc_stdev





# =============================================================================
# +S9 Positive Control
# =============================================================================

ps9_pc_avgcytox = fun.avg(
    [100 - (((fixtox.at[3,8] * fixtox.at[105,2]) 
     / fixtox.at[10,8]) * 100),
     100 - (((fixtox.at[3,8] * fixtox.at[110,2]) 
     / fixtox.at[10,8]) * 100)])

ps9_pc_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 95, 5, 95, 3), 
     fun.pcnt(MNC, 100, 5, 100, 3)]
    )
    # calculates %MNC    
    
ps9_pc_stdev = fun.stdev(
    [fun.pcnt(MNC, 95, 5, 95, 3), 
     fun.pcnt(MNC, 100, 5, 100, 3)]
    )    
    # standard deviation of percent MNC
    
ps9_pc_foldinc = ms9_pc_avgpcntMNC / ms9_vc_avgpcntMNC
    # from mean fold increase columnn on short term data summary sheet of assay            





HDB_sheet_df.at[cell, 21] = ps9_pc_avgcytox
HDB_sheet_df.at[cell, 22] = ps9_pc_avgpcntMNC
HDB_sheet_df.at[cell, 23] = ps9_pc_stdev





# =============================================================================
# +S9 Lab Reference
# =============================================================================

ps9_ref_avgcytox = fun.avg(
    [100 - (((fixtox.at[3,8] * fixtox.at[115,2]) 
     / fixtox.at[10,8]) * 100),
     100 - (((fixtox.at[3,8] * fixtox.at[120,2]) 
     / fixtox.at[10,8]) * 100)]
    )

ps9_ref_avgpcntMNC = fun.avg(
    [fun.pcnt(MNC, 105, 5, 105, 3), 
     fun.pcnt(MNC, 110, 5, 110, 3)]
    )
    # calculates %MNC
    
ps9_ref_stdev = fun.stdev(
    [fun.pcnt(MNC, 105, 5, 105, 3), 
     fun.pcnt(MNC, 110, 5, 110, 3)]
    )    
    # standard deviation of percent MNC
    




HDB_sheet_df.at[cell, 24] = ps9_ref_avgcytox
HDB_sheet_df.at[cell, 25] = ps9_ref_avgpcntMNC
HDB_sheet_df.at[cell, 26] = ps9_ref_stdev
