FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt && apk add --no-cache dumb-init

COPY . .

EXPOSE 5000

ENV FLASK_APP "backend.py"

ENTRYPOINT ["dumb-init", "--"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]