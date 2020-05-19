import os
import psycopg2

try:
    os.environ.setdefault('DATABASE_URL','postgres://uadqvrzvvhsgvl-1:76e9e53176d897f8bb1290fec47bcdde69043710aecb602067de96961e1c7bc0@ec2-107-21-126-201.compute-1.amazonaws.com:5432/d7d2gs1qbqj579')
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    print ( "PostgreSQL connection is open" )

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM hr;")
    # print(cur.fetchone())
    records = cur.fetchall()

    print("Print each row and it's columns values")
    for row in records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

    # Make the changes to the database persistent
    # conn.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if(conn):
        # Close communication with the database
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")


