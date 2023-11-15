#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (argv.length >= 3) {
  const num = parseInt(argv[2]);
  if (typeof (num) === 'number' && num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
