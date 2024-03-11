#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileName = args[2];
const content = args[3];
fs.writeFile(fileName, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
