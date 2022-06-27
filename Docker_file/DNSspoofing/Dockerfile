FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y net-tools && \
    apt-get install nano && \
    apt-get install -y ettercap-text-only
CMD ["/bin/bash"]



#install all the tools you might want to use in your container
RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install vim -y


#the following ARG turns off the questions normally asked for location and timezone for Apache
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install apache2 -y


#change working directory to root of apache webhost
WORKDIR var/www/html



#now start the server
CMD ["apachectl", "-D", "FOREGROUND"]



