FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g servor

# make the 'app' folder the current working directory
WORKDIR /app

# set environment variable
ARG VUE_APP_BACKEND_URL
ENV VUE_APP_BACKEND_URL=$VUE_APP_BACKEND_URL

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD ["servor", "dist", "index.html", "8080"]