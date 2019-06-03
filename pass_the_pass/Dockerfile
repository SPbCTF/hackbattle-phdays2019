FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt && apk add --no-cache dumb-init

COPY . .

EXPOSE 31337

ENV FLASK_APP "pass_the_pass.py"
ENV SECRET_KEY "***///kek"

ENTRYPOINT ["dumb-init", "--"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "31337"]
