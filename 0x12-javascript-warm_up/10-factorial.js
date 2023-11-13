#!/usr/bin/node

function factorize(a) {
  if (a < 0) {
    return (-1);
  }
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  return (a * factorize(a - 1));
}

console.log(factorize(Number(process.argv[2])));
