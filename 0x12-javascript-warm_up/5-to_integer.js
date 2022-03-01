#!/usr/bin/node

let result = parseInt(process.argv[2]);
if (isNaN(result)) {
  result = 'Not a number';
} else {
  result = ('My number: ' + result);
}
console.log(result);
