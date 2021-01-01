"use strict";

const express = require("express");
const router = express.Router();


const dashboard = require("./controllers/dashboard.js");
const forecast = require("./controllers/forecast.js");


router.get("/", dashboard.index);
router.get("/dashboard", dashboard.index);
router.get("/forecast", forecast.index);





module.exports = router;
