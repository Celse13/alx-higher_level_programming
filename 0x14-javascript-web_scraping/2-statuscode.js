#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, request) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${request.statusCode}`);
  }
});
