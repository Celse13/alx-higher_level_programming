#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, request, body) => {
  if (error) console.log(error);
  const numberOfOccurences = body.split('/people/18/').length - 1;
  console.log(numberOfOccurences);
});
