#!/usr/bin/node
const a = process.argv.slice(2);
let b = [];
if (a.length < 2) {
  console.log(0);
} else {
  b = a.sort(sortarray);
  b.pop();
  console.log(parseInt(b[b.length - 1]));
}

function sortarray (array) {
  return (a - b);
}
