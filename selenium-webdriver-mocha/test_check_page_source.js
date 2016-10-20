var webdriver = require('selenium-webdriver');
var chai = require('chai');
var expect = chai.expect;
var util = require('util');
var events = require('events');
var test = require('selenium-webdriver/testing');
var after = require("mocha").after;


const By = webdriver.By;
const until = webdriver.until;
const global_test_suit_timeout = 60000;
const wait_for_element_timeout = 5000;

const email = 'xxx@xxx.xxx';
const user_name = 'xxx';
const password = 'xxx';


function LoginPage() {
    this.login_field_id = 'user_login';
    this.password_field = 'user_pass';
    this.login_button = 'wp-submit';

}

LoginPage.prototype.login = function(driver) {
    driver.get('http://roman_artbees:' + password + '@roman.artbees.net/jupiter5/wp-login.php');
    driver.switchTo().alert().accept();
    driver.wait(until.elementLocated(By.id(loginPage.login_field_id)), wait_for_element_timeout).sendKeys(email);
    driver.wait(until.elementLocated(By.id(loginPage.password_field)), wait_for_element_timeout).sendKeys(password);
    driver.wait(until.elementLocated(By.name(loginPage.login_button)), wait_for_element_timeout).then(function () {
        return driver.executeScript("document.getElementsByName('" + loginPage.login_button +"')[0].click();");
    });

};


function Dashboard() {
    this.cache_link_text_css = '#wp-admin-bar-site-name > a:nth-child(1)';
}

Dashboard.prototype.wait_for_load = function(driver) {
    return driver.wait(until.elementLocated(By.css(dashPage.cache_link_text_css)), wait_for_element_timeout);

};

function Site() {
    this.url = 'http://roman.artbees.net/jupiter5/';
    this.cache_link_text = 'Clear Theme Cache';
    this.cache_link_text_css = '#wp-admin-bar-site-name > a:nth-child(1)';
    this.logo_css = '.mk-sticky-logo';
}

Site.prototype.in_source = function(driver, text_pattern) {

    driver.get(site.url).then(function () {
        driver.wait(until.elementLocated(By.css(site.logo_css)), wait_for_element_timeout);
    }).then(function () {
        driver.wait(until.elementLocated(By.linkText(site.cache_link_text)), wait_for_element_timeout).click().
        then(function () {
            driver.sleep(wait_for_element_timeout);
        }).
        then(
            driver.getPageSource().then(function (opt_callback, opt_errback) {
                try {
                    expect(opt_callback).to.contain(text_pattern);
                    console.log(text_pattern + ' was found as expected...');
                    return driver;
                }
                catch (opt_errback) {
                    console.log(text_pattern + ' \nSeems we have a problem with ' + text_pattern + '...');
                    driver.close().then(function () {
                        chai.assert(false, text_pattern + ' is not found in the page source');
                    });

                }
            })
        );
    });
};


Site.prototype.not_in_source = function(driver, text_pattern) {

    driver.get(site.url).then(function () {
        driver.wait(until.elementLocated(By.css(site.logo_css)), wait_for_element_timeout);
    }).then(function () {
        driver.getPageSource().then(function (opt_callback, opt_errback) {
            try {
                expect(opt_callback).not.to.contain(text_pattern);
                console.log(text_pattern + ' was not found as expected...');
            }
            catch (opt_errback) {
                console.log(text_pattern + ' \nSeems we have a problem with ' + text_pattern + '...');
                driver.close();
                chai.assert(false, text_pattern + ' is found in the page source');
            }
        })
    });
};

test.it('check file in source code', function (done) {
    this.timeout(global_test_suit_timeout);
    var driver = require('./driver').getDriver();

    loginPage = new LoginPage();
    dashPage = new Dashboard();
    site = new Site();


    loginPage.login(driver);
    dashPage.wait_for_load(driver);
    site.in_source(driver, 'non cached');
    site.not_in_source(driver, 'non cached');
    site.in_source(driver, 'components-production.min');

    driver.quit.then(done());

    after(function(driver) {
        driver.quit();
    });

});
