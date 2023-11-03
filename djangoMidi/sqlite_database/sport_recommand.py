import database_tool as d_t
import tens
import numpy as np
import pandas as pd
#name,height,weight,target,status,uid
def total_output(name,height,weight,target,status):
    print("name")
    user_input = [name,height,weight,target,status]
    test_data = pd.DataFrame([user_input],columns=["name","height","weight","target","status"])
    
    jpd = tens.tens_model_jpd(test_data)
    wpd = tens.tens_model_wpd(test_data)
    jog = list(jpd)
    walk = list(wpd)
    c = (jog[0][0],walk[0][0])
   
   
    
    return(c)
