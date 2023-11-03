#import csv to data.sql
def translate_csv_to_db(csv_name,DataBase_name,table_name):
    import pandas as pd
    import sqlite3 as sq
    
    #step1 load datafile from csv
    #parameter = csvName
    df = pd.read_csv(csv_name)  #"dailyCalories_merged.csv"
    
    #step2 data clean up
    df.columns = df.columns.str.strip()
    
    #step3 connect to sqlite
    #parameter = database name
    connection = sq.connect(DataBase_name) #'exercise_data_test.db'
    
    #step4 load datafile to sqlite 
    #the first parameter means the name of the table
    #the second parameter means the way to connect the db
    #if_exists is not necessery,it is used to decide the activity as the table is exist
    df.to_sql(table_name, connection, if_exists='replace')
    
    #step5 close connection
    connection.close()
    
#translate sql.db to dataframe which can be used to train ai model
def translate_sqldb_to_dataframe(DataBase_name, Table_name):
    import pandas as pd
    import sqlite3 as sq
    connection = sq.connect(DataBase_name)
    sql = pd.read_sql_query("select * from "+Table_name,connection)
    df = pd.DataFrame(sql)
    return df





#algrithm for revising output
def revising_output(output,years):
    import numpy as np
    if(years<30):
        return output
    if(years>=30):
        #here need to design the algrithm to sub the output
        return output
    
def compute_bmi(height,weight):
     height = height/100
     bmi = weight/(height*height)
     return format(bmi, '.2f')
 
 