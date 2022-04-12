#!/usr/bin/node
// script that returns the status code

const url = process.argv[2];
const request = require('request');

request(url, function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
