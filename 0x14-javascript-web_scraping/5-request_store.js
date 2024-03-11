#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const fileName = args[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(fileName, body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
