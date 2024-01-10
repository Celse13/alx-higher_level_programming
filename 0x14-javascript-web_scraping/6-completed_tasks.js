#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (error, request, body) => {
  if (error) console.log(error);
  const temp = {};
  for (const todo of body) {
    if (todo.completed) {
      temp[todo.userId] = (temp[todo.userId] || 0) + 1;
    }
  }
  console.log(temp);
});
