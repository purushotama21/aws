import psycopg2
conn = psycopg2.connect(
    host="redshift-cluster-1.cuwutbeukp73.us-east-1.redshift.amazonaws.com",
    database="dev",
    user="awsuser",
    port=5439,
    password="Admin123")
cur = conn.cursor()
# cur.execute("CREATE TABLE test (id integer PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
# a=cur.execute("SELECT * FROM users;")
# print(a)
print("connection succussfully established")
cur.execute("CREATE TABLE mytable (id int primary key, data text);")

cur.execute("INSERT INTO mytable VALUES (1,'one'), (2,'two');")
