var express = require('express');
var app = express();
var test = require('./test');

app.use('/test', test);

module.exports = app;
