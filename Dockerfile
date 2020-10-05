# Use the official image as a parent image.
FROM ubuntu:18.04
MAINTAINER Sunandita Patra <patras@umd.edu>

RUN apt-get clean all
RUN apt-get -y update
RUN apt-get -y install wget
RUN apt-get -y install python3 python3-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-tk
RUN pip3 install numpy

ADD . /app/rae
WORKDIR /app/rae/RAE_and_RAEplan
#ENTRYPOINT ["python3", "testRAEandRAEplan.py", "-h"]
ENTRYPOINT ["python3", "testRAEandRAEplan.py", "--domain", "CR", "--problem", "problem1101"]
