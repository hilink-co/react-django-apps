# Use an official node runtime as a parent image
FROM node:20

WORKDIR /app/frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/frontend/node_modules/.bin:$PATH

# Add rest of the client code
COPY . /app/frontend

EXPOSE 3001

CMD ["npm", "start"]
