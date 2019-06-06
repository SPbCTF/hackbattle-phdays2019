FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev python3-venv build-essential nginx supervisor
COPY . /usr/share/nginx/html/jaw/
COPY git /usr/share/nginx/html/jaw/.git
RUN chmod -R 755 /usr/share/nginx/html/jaw/ 
WORKDIR /usr/share/nginx/html/jaw/
RUN python3 -m venv env
RUN env/bin/pip3 install -r requirements.txt
RUN env/bin/pip3 install gunicorn
COPY jaw.conf /etc/supervisor/conf.d/jaw.conf
COPY virtual.conf /etc/nginx/conf.d/virtual.conf
RUN chmod +x ./start.sh
EXPOSE 9000
ENTRYPOINT [ "./start.sh" ]