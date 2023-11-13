#!/usr/bin/node
if (process.argv.length > 2) {
	const argument_length = process.argv.length - 2;

	for (let i = 0; i < argument_length; i++) {
		console.log(process.argv[2 + i]);
	}
}
