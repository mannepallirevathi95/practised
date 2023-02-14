import psycopg2
try:
    connection = psycopg2.connect(host = "localhost",
                            port = "5432",
                            database="postgres",
                            user = "postgres", 
                            password = "sridevi123")
    cursor = connection.cursor()
    emp_table_cr = 'create table command'
    cursor.execute(emp_table_cr)
    connection.commit()
except Exception as exec:
    print("Exception occured : ", exec)
finally:
    cursor.close()
    connection.close()