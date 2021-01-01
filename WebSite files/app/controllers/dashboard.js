"use strict";

const logger = require("../utils/logger");


const dashboard = {
  index(request, response) {
    logger.info('dashboard rendering');
    const viewData = {
      title: 'Dashboard',
    };
    logger.info('about to render');
    response.render('dashboard', viewData);
  },
};

module.exports = dashboard;