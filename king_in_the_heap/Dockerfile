FROM debian:stable-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -yq socat util-linux

WORKDIR /usr/src/app

COPY server run.sh ./

RUN chmod +x run.sh && chmod +x server

CMD ["./run.sh"]


