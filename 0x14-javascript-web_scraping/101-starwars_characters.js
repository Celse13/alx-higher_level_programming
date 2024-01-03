#!/usr/bin/node
const request = require('request');
const util = require('util');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const promisifiedRequest = util.promisify(request);

(async () => {
  try {
    const filmBody = (await promisifiedRequest(url, { json: true })).body;
    for (const characterUrl of filmBody.characters) {
      const characterBody = (await promisifiedRequest(characterUrl, { json: true })).body;
      console.log(characterBody.name);
    }
  } catch (error) {
    console.log(error);
  }
})();
