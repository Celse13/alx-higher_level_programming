#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let num = parseInt(process.argv[2]);

  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
