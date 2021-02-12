var express = require('express');
const request = require('request');

var router = express.Router();

router.get('/', (req, res) => {
    request('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', { json: true }, (err, rs, body) => {
        if (err) { return console.log(err); }
        res.send(body);
    });
});

module.exports = router;