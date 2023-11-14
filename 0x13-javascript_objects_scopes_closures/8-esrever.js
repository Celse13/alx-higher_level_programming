#!/usr/bin/node
exports.esrever = function (list) {
  const newReverse = [];
  for (let i = list.length; i >= 0; i--) {
    newReverse.push(list[i]);
  }
  return newReverse;
};
