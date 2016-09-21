#
# Java Monitor: jvmtop Dockerfile
#

FROM ubuntu:16.04

ENV JVMTOP_VERSION 0.8.0    

# Download jvmtop and unzip the tar package

RUN \
    curl https://github.com/patric-r/jvmtop/releases/download/0.8.0/jvmtop-$JVMTOP_VERSION.tar.gz | tar zxf - &&\
    
WORKDIR /root
