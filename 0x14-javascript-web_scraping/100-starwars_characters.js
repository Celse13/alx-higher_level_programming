#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (const characterUrl of body.characters) {
      request(characterUrl, { json: true }, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.log(characterError);
        } else {
          console.log(characterBody.name);
        }
      });
    }
  }
});
