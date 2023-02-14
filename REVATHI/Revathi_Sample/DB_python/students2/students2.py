import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            database="students",
                            user="postgres",
                            password="sridevi123")
    print("Connection object : ", type(conn), conn)

    # Step2 : Get cursor on db connection
    cursor = conn.cursor()
    print("Cursor object : ", type(cursor), cursor)

    # Step3: Prepare SQL Query
    query = "CREATE TABLE STUDENT2(student_id INTEGER PRIMARY KEY, name VARCHAR(100), school VARCHAR(20))"

    # Step4 : Execute SQL query
    cursor.execute(query)

    # Step5: Commit the transaction
    conn.commit()
    print("** Table created successfully **")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()

conn.commit()

conn.close()
