FROM ubuntu

RUN apt-get update \
	&& apt install -y \
		python3.8 \
		python3-pip

# Here we get all python packages.
# Pip leaves the install caches populated which uses a significant amount of 
# space. These optimizations save a fair amount of space in the image, which 
# reduces start up time.
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r \
	requirements.txt

# Copy the content of the repository to the Docker.
ADD ./* $HOME/42AI/
# Set the working directory for all the subsequent Dockerfile instructions.
WORKDIR $HOME/42AI/