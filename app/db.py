import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="Smart-Delivery",
        user="postgres",
        password="Hojlund1099@"  # Replace with your PostgreSQL password
    )
