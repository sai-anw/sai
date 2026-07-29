FROM ubuntu:latest
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates python3 python3-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN mkdir -p /app
#RUN pip3 install --no-cache-dir -r requirements.txt
#RUN pip3 install --no-cache-dir flask

#see you
run touch 1.txt

#hi
#bye
#see you

