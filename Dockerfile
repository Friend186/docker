# Use the official Ultralytics image specifically built for NVIDIA Jetson devices
FROM ultralytics/ultralytics:latest-jetson

# Set our working directory inside the container
WORKDIR /workspace

# Uninstall the broken new versions
RUN pip uninstall -y opencv-python opencv-python-headless

# Install Kaggle AND explicitly install an older version of headless OpenCV 
# that is compatible with Ubuntu 20.04
RUN pip install kaggle "opencv-python-headless<4.9"

# Copy our Python script into the container
COPY test.py .

# Run the script when the container turns on
CMD ["python3", "test.py"]