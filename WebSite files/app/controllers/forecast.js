"use strict";

const logger = require("../utils/logger");


const forecast = {
  index(request, response) {
    logger.info('forcast rendering');
    const viewData = {
      title: 'Forecast',
    };
    logger.info('about to render');
    response.render('forecast', viewData);
  }, 
};
  

module.exports = forecast;