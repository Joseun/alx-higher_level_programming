#!/usr/bin/node
// script that returns the Star Wars Movies

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(results);
});
