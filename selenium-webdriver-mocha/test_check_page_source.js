var webdriver = require('selenium-webdriver');
var test = require('selenium-webdriver/testing');
var chai = require('chai');
var expect = chai.expect;
var driver = require('./driver').getDriver();

const By = webdriver.By;
const until = webdriver.until;
const global_test_suit_timeout = 60000;
const wait_for_element_timeout = 5000;

const company_name = 'xxx';
const user_name = 'xxx';
const email = user_name + '@' + company_name + '.net';
const password = 'xxx';
const login = user_name + '_' + company_name;

function Page () {
    this.page_time_out = 5000;
}

Page.prototype.waitForPage = function (driver){
    driver.wait(function () {
        return driver.executeScript('return document.readyState === "complete"');
    }, this.page_time_out);
};

Page.prototype.checkTitle = function (driver, page_title){
    driver.wait(function() {
        return driver.getTitle().then(function(title) {
            return title === page_title;
        });
    }, wait_for_element_timeout);
};


function LoginPage() {
    this.login_field_id = 'user_login';
    this.password_field = 'user_pass';
    this.login_button = 'wp-submit';
    this.page_title = "Jupiter WordPress Theme ‹ Log In";


}

LoginPage.prototype = Object.create(Page.prototype);
LoginPage.prototype.constructor = LoginPage;

LoginPage.prototype.login = function(driver) {
    this.waitForPage(driver);
    this.checkTitle(driver, this.page_title);
    driver.wait(until.elementLocated(By.id(loginPage.login_field_id)), wait_for_element_timeout).sendKeys(email);
    driver.wait(until.elementLocated(By.id(loginPage.password_field)), wait_for_element_timeout).sendKeys(password);
    driver.wait(until.elementLocated(By.name(loginPage.login_button)), wait_for_element_timeout).then(function () {
        console.log('Login to website...');
        return driver.executeScript("document.getElementsByName('" + loginPage.login_button +"')[0].click();");
    });
};


function Dashboard() {
    this.cache_link_text_css = '#wp-admin-bar-site-name > a:nth-child(1)';
    this.page_title = 'Dashboard ‹ Jupiter WordPress Theme — WordPress';
    this.page = new Page();
}

Dashboard.prototype = Object.create(Page.prototype);
Dashboard.prototype.constructor = Dashboard;

Dashboard.prototype.waitForPageToLoad = function(driver) {
    this.waitForPage(driver);
    this.checkTitle(driver, this.page_title);
    return driver.wait(until.elementLocated(By.css(dashPage.cache_link_text_css)), wait_for_element_timeout).then(function () {
        console.log('Wait for page Dashboard ...');
    });

};


function Site() {
    this.url = 'http://roman.artbees.net/jupiter5/';
    this.cache_link_text = 'Clear Theme Cache';
    this.cache_link_text_css = '#wp-admin-bar-site-name > a:nth-child(1)';
    this.logo_css = '.mk-sticky-logo';
    this.page_title = 'Main Demo - Jupiter WordPress Theme';
}

Site.prototype = Object.create(Page.prototype);
Site.prototype.constructor = Site;

Site.prototype.waitForPageToLoad = function(driver) {
    this.waitForPage(driver);
    this.checkTitle(driver, this.page_title);
    return driver.wait(until.elementLocated(By.css(this.logo_css)), wait_for_element_timeout).then(function () {
        console.log('Wait for page Site ...');
    });

};

Site.prototype.openPage = function(driver) {
    driver.get(this.url);
    this.waitForPageToLoad(driver).then(function () {
        console.log('Open page Site ...');
    });
};

Site.prototype.cleanSiteCache = function(driver) {
    driver.wait(until.elementLocated(By.linkText(this.cache_link_text)), wait_for_element_timeout).click();
    return this.waitForPageToLoad(driver).then(function () {
        driver.sleep(wait_for_element_timeout).then(function () {
            console.log('Clean cache ...');
        });
    });
};

Site.prototype.inSource = function(driver, text_pattern) {
    this.waitForPageToLoad(driver).then(
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
};

Site.prototype.notInSource = function(driver, text_pattern) {
    driver.wait(until.elementLocated(By.linkText(this.cache_link_text)), wait_for_element_timeout).click();
    this.waitForPageToLoad(driver).then(function () {
        driver.sleep(wait_for_element_timeout);
    }).then(
        driver.getPageSource().then(function (opt_callback, opt_errback) {
            try {
                expect(opt_callback).to.contain(text_pattern);
                console.log(text_pattern + 'was not found as expected...');
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
};


beforeEach(function(done) {
    this.timeout(global_test_suit_timeout);
    var callback = arguments[arguments.length - 1];
    driver.get('http://roman_' + company_name + ':' + password + '@roman.'+ company_name + '.net/jupiter5/wp-login.php').then(function () {
        driver.switchTo().alert().accept();
        done();
    });
});


afterEach(function(done) {
    driver.quit().then(done);
});


test.it('check pattern in source code', function (done) {
    this.timeout(global_test_suit_timeout);
    loginPage = new LoginPage();
    dashPage = new Dashboard();
    site = new Site();


    loginPage.login(driver);
    dashPage.waitForPageToLoad(driver);


    site.openPage(driver);
    site.cleanSiteCache(driver);
    site.inSource(driver, 'non cached');
    site.openPage(driver);
    site.notInSource(driver, 'non cached');
    done();

});
