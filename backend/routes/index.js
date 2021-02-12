var express = require('express');
var app = express();
var test = require('./test');
var weather = require('./weather');

app.use('/test', test);
app.use('/weather', weather)

module.exports = app;
