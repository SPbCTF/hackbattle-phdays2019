FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk add --no-cache dumb-init netcat-openbsd

COPY . .

RUN mv flag /opt/flag

EXPOSE 5000
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python", "main.py"]
