var express = require('express');
var routes = require('./routes/index');

var app = express();

app.use('/api/v1', routes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () =>{
	console.log('Listing on port ' + PORT);
});

module.exports = app;
