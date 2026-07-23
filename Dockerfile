# ---------------------------------------------------------
# IRON LOGIC: Localized GPU Automation Runner
# ---------------------------------------------------------

# Choose a specialized base image for hardware acceleration
FROM nvidia/cuda:12.1.1-base-ubuntu22.04

# Set the working directory inside the container
WORKDIR /opt/iron-logic

# Install essential infrastructure tools and Python
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy local dependency requirements to the container
COPY requirements.txt .

# Install external Python libraries 
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the core infrastructure payloads into the working directory
COPY production/ .

# Execute the Day-2 Ops matrix on boot
CMD ["python3", "vram_zombie_killer.py"]