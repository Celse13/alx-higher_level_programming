#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let num = parseInt(process.argv[2]);
	let i = 0;
  while (i < num) {
		console.log('X'.repeat(num));
    i++;
  }
}
