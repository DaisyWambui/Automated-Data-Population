import mysql.connector
import schedule
import time
from faker import Faker

# Initialize Faker
fake = Faker()

# MySQL Database Configuration
db_config = {
    'host': 'localhost',  
    'port': 3310,    
    'user': 'dwambui',   
    'password': 'dwambui@2024',  
    'database': 'project1_db'   
}

# Function to create table if not exists
def create_table():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL,
            address TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table checked/created successfully.")

    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

# Function to generate and insert data
def generate_and_insert_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Generate Fake Data
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        phone = fake.phone_number()
        address = fake.address()

        # Insert Data into MySQL
        insert_query = """
        INSERT INTO users (first_name, last_name, email, phone, address) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (first_name, last_name, email, phone, address)

        cursor.execute(insert_query, values)
        conn.commit()

        print(f"Inserted: {first_name} {last_name} - {email}")

        # Close DB Connection
        cursor.close()
        conn.close()
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Ensure the table exists before inserting data
create_table()

# Schedule task every 1 minutes
schedule.every(1).minutes.do(generate_and_insert_data)

print("Data generation started. Press Ctrl+C to stop.")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
