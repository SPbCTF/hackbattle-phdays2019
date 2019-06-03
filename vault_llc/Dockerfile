FROM node:alpine

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn

COPY . .

ENV flag "battles{never_parse_user_input_structures!!!}"

EXPOSE 31337
CMD ["yarn", "start"]