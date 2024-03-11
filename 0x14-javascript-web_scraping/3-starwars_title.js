#!/usr/bin/node
const request = require('request');
const args = process.argv;
const id = args[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
