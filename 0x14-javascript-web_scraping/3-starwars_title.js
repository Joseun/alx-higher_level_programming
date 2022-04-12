#!/usr/bin/node
// script that returns the Star Wars Movies

const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
