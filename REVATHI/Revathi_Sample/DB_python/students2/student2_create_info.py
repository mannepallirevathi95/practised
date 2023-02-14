import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="students",
                            user="postgres",
                            password="sridevi123",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()

    records = [(101, 'MADHU', 'ABC'), (102, 'Prakash', 'AREM'), (103, 'Kiran', 'VN2')]
    query = "INSERT INTO STUDENT2 VALUES(%s, %s, %s)"
    count = 0

    for record in records:
        cursor.execute(query, record)
        count += 1
        print("Query executed")
    print("Query execution : ", count)


    
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")

except Exception as exce:
    print("Exception occured : ",exce)

finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()