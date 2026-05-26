# Use the official Ultralytics image specifically built for NVIDIA Jetson devices
FROM ultralytics/ultralytics:latest-jetson

# Set our working directory inside the container
WORKDIR /workspace

# Install the Kaggle API tool
RUN pip install kaggle

# Copy our Python script into the container
COPY test.py .

# Run the script when the container turns on
CMD ["python3", "test.py"]