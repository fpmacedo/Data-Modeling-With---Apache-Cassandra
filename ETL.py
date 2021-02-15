# Import Python packages 
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from sql_queries import * 
from create_csv import create_csv


def db_conect():
    # This should make a connection to a Cassandra instance your local machine 
    # (127.0.0.1)

    from cassandra.cluster import Cluster
    cluster = Cluster(['127.0.0.1'])

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    
    # TO-DO: Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('sparkifydb')
    except Exception as e:
        print(e)
        
    return session, cluster

def process_csv(filepath, new_csv_name):
    
    #Create the csv file using the filepath and the name of the new csv file
    create_csv(filepath, new_csv_name)

    # check the number of rows in your csv file
    with open(new_csv_name + '.csv', 'r', encoding = 'utf8') as f:
        print(sum(1 for line in f))
    

def insert_data(file, session):
        # We have provided part of the code to set up the CSV file. Please complete the Apache Cassandra code below#
    with open((file +'.csv'), encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
    ## TO-DO: Assign the INSERT statements into the `query` variable
            session.execute(insert_query1_table, (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
            session.execute(insert_query2_table, (line[0], line[9], line[1], line[4], int(line[8]), int(line[3]), int(line[10])))
            session.execute(insert_query3_table, (line[9], line[1], line[4]))
        
def select_data(session):
    
    ## TO-DO: Query 1:  Give me the artist, song title and song's length in the music app history that was heard during \
    ## sessionId = 338, and itemInSession = 4
    ## TO-DO: Add in the SELECT statement to verify the data was entered into the table
    rows1 = session.execute(select_query1_table)
        
    print("1 - Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4: ")
    
    for row1 in rows1:
        print (row1.artist, row1.song, row1.length)
    print (" ")
        
    ## TO-DO: Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name)\
    ## for userid = 10, sessionid = 182
    rows2 = session.execute(select_query2_table)
        
    print("2 - Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182: ")
    
    for row2 in rows2:
        print (row2.artist, row2.song)
    print (" ")
        
    ## TO-DO: Query 3: Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
    rows3 = session.execute(select_query3_table)

    print("3 - Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own': ")
    
    for row3 in rows3:
        print (row3.firstname, row3.lastname)
    print (" ")
    
    
def main():
    """
    Build ETL Pipeline for Sparkify song play data:
    
    Instantiate a session to the Postgres database, 
    acquire a cursor object to process SQL queries,
    and process both the song and the log data.    
    """
    
    session, cluster = db_conect()
    
    # checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'
    file_name = 'event_datafile_new'
    process_csv(filepath, file_name)
    insert_data(file_name, session)
    select_data(session)
    
    #falta finalizar a parte de selecionar os dados e printar
    
  

    session.shutdown()
    cluster.shutdown()

   

if __name__ == "__main__":
    main()