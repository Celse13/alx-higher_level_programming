#!/usr/bin/node
exports.esrever = function (list) {
  const newReverse = [];
  for (const element of list) {
    newReverse.unshift(element);
  }
  return newReverse;
};
