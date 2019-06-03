FROM node:alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn

COPY . .

ENV flag "battles{beware_pr0tp0l}"

EXPOSE 31337
CMD ["yarn", "start"]