#!/usr/bin/node
const request = require('request');
const args = process.argv;
request.get(args[2], (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code:', response.statusCode);
});
