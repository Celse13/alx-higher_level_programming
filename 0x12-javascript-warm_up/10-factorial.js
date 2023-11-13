#!/usr/bin/node
const process = require('process');

function factorial(a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a < 0) {
    return -1;
  } else if (a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

console.log(factorial(parseInt(process.argv[2])));
