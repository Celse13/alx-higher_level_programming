#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, request, body) => {
  if (error) console.log(error);
  console.log(body.title);
});
