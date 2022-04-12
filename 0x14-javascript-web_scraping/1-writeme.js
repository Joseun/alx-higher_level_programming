#!/usr/bin/node
// script that writes content into a file

const file = process.argv[2];
const words = process.argv[3];
const fs = require('fs');

fs.writeFile(file, 'utf8', words, error => {
  if (error) {
    console.log(error);
  }
});
