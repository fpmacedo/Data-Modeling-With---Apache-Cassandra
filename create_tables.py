import cassandra
from sql_queries import * 


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # This should make a connection to a Cassandra instance your local machine 
    # (127.0.0.1)

    from cassandra.cluster import Cluster
    cluster = Cluster(['127.0.0.1'])

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    
    # TO-DO: Create a Keyspace 
    try:
        session.execute(create_keyspace)

    except Exception as e:
        print(e)
        
    # TO-DO: Set KEYSPACE to the keyspace specified above
    try:
        session.set_keyspace('sparkifydb')
    except Exception as e:
        print(e)
   
    
    return session, cluster


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        session.execute(query)


def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        session.execute(query)


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    session, cluster = create_database()
    
    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()