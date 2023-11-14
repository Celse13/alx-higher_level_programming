#!/usr/bin/node
const list = require('./100-data').list;
const mapping = list.map((u, v) => u * v);
console.log(list);
console.log(mapping);
