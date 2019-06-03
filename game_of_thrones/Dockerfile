FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk add --no-cache dumb-init

COPY . .

EXPOSE 10000
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python", "task.py"]
