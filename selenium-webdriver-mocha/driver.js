var getDriver;
getDriver = function () {
    const webdriver = require('selenium-webdriver');
    const Capabilities = require('selenium-webdriver/lib/capabilities').Capabilities;

    var capabilities = Capabilities.firefox();

    capabilities.set('marionette', true);

    return new webdriver.Builder().withCapabilities(capabilities).build();
};

module.exports.getDriver = getDriver;