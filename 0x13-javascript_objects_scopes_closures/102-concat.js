#!/usr/bin/node
const readFile = require('fs');

const readOne = readFile.readFileSync(process.argv[2]).toString();
const readTwo = readFile.readFileSync(process.argv[3]).toString();
readFile.writeFileSync(process.argv[4], readOne + readTwo);
