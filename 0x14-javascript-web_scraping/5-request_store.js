#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const readMe = process.argv[3];

request(url, (error, request, body) => {
  if (error) console.log(error);
  try {
    fs.writeFileSync(readMe, body, 'utf-8');
  } catch (error) {
    console.error(error);
  }
});
