'use strict';

var os = require('os');
const dns = require('dns');

const express = require('express');

// Constants
const PORT = 8080;

// App
const app = express();
app.get('/', function (req, res) {

	var hostname = os.hostname();

	res.send('hostname: ' + hostname);
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);

