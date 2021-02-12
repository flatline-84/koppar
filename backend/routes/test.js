var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
	res.send("GET route on TEST");
});

router.post('/', (req, res) => {
	return res.send("POST route on TEST");
});

module.exports = router;
