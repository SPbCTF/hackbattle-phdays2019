FROM debian:latest

EXPOSE 18800

RUN apt-get update
RUN apt-get -y install open-cobol xinetd

WORKDIR /root/storage
COPY . .
RUN cobc -free -x -o storage.elf super_security_storage.CBL
RUN cp xinetd.conf /etc/xinetd.d/storage
RUN service xinetd restart

CMD script -c "xinetd -d"
