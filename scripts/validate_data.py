import snowflake.connector

conn = snowflake.connector.connect(
    user='<user>',
    password='<password>',
    account='<account>'
)

cs = conn.cursor()
try:
    cs.execute("SELECT CURRENT_VERSION()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
conn.close()
