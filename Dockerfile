# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY app/ .

# Copy the data files into the container
COPY data/ data/

# Run the main script when the container starts
CMD ["python", "main.py"]
