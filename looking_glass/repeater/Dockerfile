FROM python:alpine

RUN apk add --no-cache dumb-init

WORKDIR /usr/src/app

COPY repeater.py .

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python", "repeater.py"]
