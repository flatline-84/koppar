var express = require('express');
var routes = requite('./routes/index');

var app = express();

app.use('/api/v1', routes);

app.listen(process.env.PORT || 3000, () =>{
	console.log('Listing on port 3000');
});

module.exports = app;
