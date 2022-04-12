#!/usr/bin/node
// script that writes content into a file

const url = process.argv[2];
const file= process.argv[3];
const request = require('request');
request(url).pipe(fs.createWriteStream(file));
