#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileName = args[2];
fs.readFile(fileName, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});
