import psycopg

# Make sure you are using the password for your database whenever you installed Postgres into our machines
conn = psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres", password="J1a0c2k5")

# Retrieve a cursor object from our connection object
# Cursor objects allow us to send queries to the Postgres database
cur = conn.cursor()

# Send query to the database
cur.execute("SELECT * FROM users")

# print(cur.fetchone())   # (1, 'bachy21', '518-826-0001', True) <--tuple
# print(cur.fetchone())   # (1, 'jane_doe', '518-826-0002', True) <--tuple
# print(cur.fetchone())   # (1, 'bob123', '518-826-0003', False) <--tuple

# my_users = cur.fetchall()  # This will return a list of tuples
# print(my_users)

# You cna also directly iterate over the cursor as well to retrieve the records fom a query
# for record in cur:
#    print(record[1])


# DML - INSERT, SELECT, UPDATE, DELETE
# Insert Data

# %s serves as a placeholder for values you would like to utilize inside your query
# We create a query "template" and then provide values for each of those %s placeholders as a second argument
# in the .execute method
sql_query_template = "INSERT INTO users (username, mobile_phone) VALUES (%s, %s) RETURNING id"
cur.execute(sql_query_template, ('testing123', '512-826-0008'))
print(f"The id of the users record we just inserted is: {cur.fetchone()[0]}")

# Notice we commit using the connection object and not the cursor object
# We need to commit because psycopg by default does not automatically commit DML commands
conn.commit()

# Close the connection
conn.close()
