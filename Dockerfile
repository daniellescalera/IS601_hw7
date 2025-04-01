# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy all the project files to the container
COPY . .

# Set environment variables (You can change these when running the container if needed)
ENV QR_DATA_URL="https://github.com/daniellescalera" 
ENV QR_CODE_DIR="qr_codes"
ENV QR_CODE_FILENAME="github_qr.png"
ENV FILL_COLOR="black"
ENV BACK_COLOR="white"

# Run the Python script when the container starts
CMD ["python", "generate_qr.py"]
