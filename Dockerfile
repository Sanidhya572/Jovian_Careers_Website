FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application will run
EXPOSE 5000

# Specify the command to run the Flask application
CMD ["python", "app.py"]
