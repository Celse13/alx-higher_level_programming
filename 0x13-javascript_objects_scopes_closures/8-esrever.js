#!/usr/bin/node
exports.esrever = function (list) {
  const newReverse = [];
  for (const ele of list) {
    newReverse.unshift(ele);
  }
  return newReverse;
};
