#!/usr/bin/node

function factorial (n) {
  if (n >= 1) {
    return (n * factorial(n - 1));
  } else {
    return (1);
  }
}

const a = parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
