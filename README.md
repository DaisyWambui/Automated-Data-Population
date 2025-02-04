# Automated-Data-Population using Docker and Python
In this project, I automated the generation and insertion of synthetic user data into a MySQL database. By utilizing Python, Faker, and Docker, I developed a script that automatically generates realistic user data, streamlining the process for testing and development.

# Project Overview
This project automates the process of populating a MySQL database with randomly generated user data at regular intervals. It leverages Python, Docker, and Docker Compose for containerization and automation. A Python script generates fake user data using the Faker library and inserts it into a MySQL database. Docker ensures the environment is consistent across different setups, while Docker Compose simplifies container management.

# Key Components
# - Python Script: The main script generates fake user data and populates the MySQL database.
# - Docker: Used to containerize the MySQL database and Python environment.
# - Docker Compose: Manages the multi-container setup, ensuring the Python script can connect to the MySQL database.
# - MySQL Database: Used as the storage for the generated data.
# Steps Taken
# 1. Docker Setup
A Dockerfile was created to define the environment for running the Python script. 
The Dockerfile includes:

- Installing the necessary Python packages like mysql-connector-python, Faker, and schedule.
- Setting up a Python environment to run the script inside a Docker container.
  
The docker-compose.yml file was created to:

Define the MySQL service and set up its environment variables (e.g., root password, database name, user credentials).
Link the Python environment with the MySQL container, enabling the Python script to interact with the database.
# 2. Python Script Creation
A Python script (populate_db.py) was written to:

- Use the Faker library to generate random user data (name, email, address, etc.).
- Establish a connection to the MySQL database using mysql-connector-python.
- Create a users table in MySQL (if it doesn't exist) to store the generated data.
- Insert data into the table every minute using the schedule library for automation.
# 3. Automation
The Python script was configured to run continuously and insert data into the MySQL database at scheduled intervals (every minute). The schedule library ensures that the data population happens automatically without manual intervention.

# 4. Git Integration
A Git repository was initialized to manage the project and ensure version control. 
The project includes:

- A .gitignore file to exclude unnecessary files (like logs and virtual environments) from being pushed to GitHub.
- The entire project was committed to GitHub to make it accessible remotely for collaboration and version control.
# 5. Running the Project
Using Docker Compose, both the MySQL database and the Python script container were set up with a single command (docker-compose up --build).

The Python script ran in the Docker container, automatically populating the MySQL database with fake data at set intervals.
# 6. Database Population
Once the setup was complete, the database was verified by connecting to the MySQL container and checking the users table to ensure that it was correctly populated.
