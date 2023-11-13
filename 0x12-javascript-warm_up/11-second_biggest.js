#!/usr/bin/node

if (process.argv.length <= 3) console.log(0);
else {
  console.log(argv.slice(2).sort((x, y) => y - x)[1]);
}
