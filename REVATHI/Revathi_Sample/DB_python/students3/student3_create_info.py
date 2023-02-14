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

    records = [(201, 'SAI', 'ABC'), (202, 'MAHENDRA', 'AREM'), (203, 'VAMSI', 'VN2')]
    query = "INSERT INTO STUDENT3 VALUES(%s, %s, %s)"
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