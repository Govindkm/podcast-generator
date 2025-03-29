FROM ubuntu:latest

# Install Dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git

RUN pip3 install pyYAML --break-system-packages

COPY feed.py /usr/local/bin/feed.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]