# Use a base image with Python installed
FROM python:3.8-slim

# Set the working directory
WORKDIR /home
RUN mkdir -p /home/data /home/output
# Copy the Python script into the container
COPY . /home/data
RUN touch /home/output/result.txt

RUN chmod +x /home/data/cloud.py
RUN chmod +w /home/output/result.txt

# Run the Python script when the container starts
CMD ["python", "/home/data/cloud.py"]
