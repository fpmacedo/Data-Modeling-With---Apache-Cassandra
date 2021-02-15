#DROP TABLES

query1_table_drop = "DROP TABLE IF EXISTS query1_table"
query2_table_drop = "DROP TABLE IF EXISTS query2_table"
query3_table_drop = "DROP TABLE IF EXISTS query3_table"


#CREATE KEY SPACE

create_keyspace = (
    """
    CREATE KEYSPACE IF NOT EXISTS sparkifydb 
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
    """
                  )

#CREATE TABLE

create_query1_table =  ("""CREATE TABLE IF NOT EXISTS query1_table 
                        (
                        sessionId int,
                        itemInSession int,
                        artist text,
                        song text,
                        length float,
                        PRIMARY KEY (sessionId, itemInSession)
                        );
                    """)

create_query2_table =  ("""CREATE TABLE IF NOT EXISTS query2_table 
                        (
                        artist text,
                        song text,
                        firstName text,
                        lastName text,
                        sessionId int,
                        itemInSession int,
                        userId int,
                        PRIMARY KEY ((sessionId, userId), itemInSession )
                        );
                    """)

create_query3_table =  ("""CREATE TABLE IF NOT EXISTS query3_table 
                        (
                        song text,
                        firstName text,
                        lastName text,
                        PRIMARY KEY (song, firstName, lastName)
                        );
                    """)


#INSERT DATA IN TABLES

insert_query1_table = ("""INSERT INTO query1_table
                    (
                        sessionId,
                        itemInSession,
                        artist,
                        song,
                        length                        
                    )
                        VALUES (%s, %s, %s, %s, %s);
                    """)

insert_query2_table = ("""INSERT INTO query2_table
                    (
                        artist,
                        song,
                        firstName,
                        lastName,
                        sessionId,
                        itemInSession,
                        userId
                    )
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """)

insert_query3_table = ("""INSERT INTO query3_table
                    (
                        song,
                        firstName,
                        lastName
                    )
                        VALUES (%s, %s, %s);
                    """)

#SELECT QUERYS

select_query1_table = ("""SELECT artist, song, length
                         FROM query1_table 
                         WHERE sessionId = 338 and itemInSession = 4;
                      """)

select_query2_table = ("""SELECT artist, song
                         FROM query2_table
                         WHERE  sessionid = 182 and userid = 10
                         ORDER BY itemInSession;
                      """)

select_query3_table = ("""SELECT firstName, lastName
                         FROM query3_table
                         WHERE song = 'All Hands Against His Own';
                      """)

# QUERY LISTS

create_table_queries = [create_query1_table, create_query2_table, create_query3_table]
drop_table_queries = [query1_table_drop, query2_table_drop, query3_table_drop]
select_table_queries = [select_query1_table, select_query2_table, select_query3_table]
