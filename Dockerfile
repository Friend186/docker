# Use the official Ultralytics image specifically built for NVIDIA Jetson devices
FROM ultralytics/ultralytics:latest-jetson

# Set our working directory inside the container
WORKDIR /workspace

# Remove standard OpenCV and install the Headless version + Kaggle
RUN pip uninstall -y opencv-python opencv-python-headless && \
    pip install kaggle opencv-python-headless

# Copy our Python script into the container
COPY test.py .

# Run the script when the container turns on
CMD ["python3", "test.py"]