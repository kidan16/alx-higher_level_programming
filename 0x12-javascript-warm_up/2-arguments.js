#!/usr/bin/node
'use strict';
let arg = process.argv.length;
if (arg === 2) {
	  console.log('No argument');
} else if (arg === 3) {
	  console.log('Argument found');
} else {
	  console.log('Arguments found');
}
