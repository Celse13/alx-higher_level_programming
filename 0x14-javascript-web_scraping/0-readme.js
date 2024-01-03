#!/usr/bin/node
const fs = require('fs');
const readMe = process.argv[2];

fs.readFile(readMe, 'utf-8', (error, content) => {
  console.log(error || content);
});
