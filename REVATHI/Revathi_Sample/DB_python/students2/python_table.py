import psycopg2 as pg2

try:

    conn = pg2.connect(
    database = 'class',
    user = 'postgres',
    password = 'sridevi123'
    )

    cur = conn.cursor()

    query = "CREATE TABLE SALARY(user_id SERIAL PRIMARY KEY,
                            name VARCHAR(50),
                            salary INTEGER)""
    cur.execute(query)
    print("** Table created successfully **")

except Exception as exce:

    print("Exception occured : ", exce)

finally:
    print("Closing cursor and connection to POSTGRESQL")
    cur.close()
    conn.close()

conn.commit()

conn.close()
