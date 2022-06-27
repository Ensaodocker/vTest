FROM debian

RUN apt-get update
RUN apt-get install net-tools
RUN apt-get install -y iputils-ping
RUN apt install iproute2 -y
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
