FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents (including the script) into the container at /usr/src/app
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir mysql-connector-python faker schedule

# Expose the port that the MySQL container is using
EXPOSE 3306

# Run the script when the container starts
CMD ["python", "./populate_db.py"]