#!/usr/bin/node
const fs = require('fs');
const readMe = process.argv[2];
const readString = process.argv[3];

fs.writeFile(readMe, readString, 'utf-8', (error) => {
  if (error) console.log(error);
});
