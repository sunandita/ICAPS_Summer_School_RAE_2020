# Use the official image as a parent image.
FROM ubuntu:18.04
MAINTAINER Sunandita Patra <patras@umd.edu>

RUN apt-get clean all
RUN apt-get -y update
RUN apt-get -y install wget
RUN apt-get -y install python3 python3-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-tk
RUN pip3 install numpy

ADD . /app/ICAPS_Summer_School_RAE_2020
WORKDIR /app/ICAPS_Summer_School_RAE_2020/RAE_and_UPOM
#ENTRYPOINT ["python3", "testRAEandUPOM.py", "-h"]
ENTRYPOINT ["python3", "testRAEandUPOM.py", "--domain", "CR", "--problem", "problem1001"]
