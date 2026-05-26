# Use the Ultralytics image specifically built for JetPack 6 (Ubuntu 22.04)
FROM ultralytics/ultralytics:latest-jetson-jetpack6

# Set our working directory inside the container
WORKDIR /workspace

# Install Kaggle and the headless version of OpenCV
RUN pip uninstall -y opencv-python opencv-python-headless && \
    pip install kaggle opencv-python-headless

# Copy our Python script into the container
COPY test.py .

# Run the script
CMD ["python3", "test.py"]