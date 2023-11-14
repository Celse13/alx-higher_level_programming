#!/usr/bin/node
const dict = require('./101-data').dict;
const dictionary = {};
for (const keyFinding in dict) {
  if (dictionary[dict[keyFinding]] === undefined) {
    dictionary[dict[keyFinding]] = [];
  }
  dictionary[dict[keyFinding]].push(keyFinding);
}
console.log(dictionary);
