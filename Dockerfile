FROM ubuntu:16.04
# set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1


EXPOSE 8010
WORKDIR /setup

# Update the default application repository sources list
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    build-essential \
    python3-dev \
    libpq-dev \
    postgresql \
    libsasl2-dev \ 
    libldap2-dev \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-gdbm \
    git

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /usr/src/app

# Copy the rest of the application's code
COPY . /usr/src/app
