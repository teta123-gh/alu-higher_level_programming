#!/usr/bin/node
const arg = process.argv[2];
const numberOccurrences = parseInt(arg);
if (isNaN(numberOccurrences)) console.log('Missing number of occurrences');
else for (let i = 0; i < numberOccurrences; i++) console.log('C is fun');
