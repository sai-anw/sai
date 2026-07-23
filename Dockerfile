FROM ubuntu:latest
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates python3 python3-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN mkdir -p /app