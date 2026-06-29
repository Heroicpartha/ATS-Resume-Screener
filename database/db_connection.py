import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="resume_screener",
    user="postgres",
    password="partha@123",
    port="5433"
)

print("Connected Successfully!")