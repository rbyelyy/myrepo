#!/bin/sh
# This script helps to set up necessary environment for starting developing
# Cursera "Startup Engineering" course. 
# Clone repo Navigate to report
# Create 2 git branches development and staging and update them based on the github branches
# Install heroku and nmp if necessary
# Update port in web.js
# Clone repository for bitstarter
# Login into Heroku (adding rsa keys)
# Create two Heroku apps
# Push code to staging and production branches of Heroku 
# Tip 'How to create keys' ssh-keygen -t rsa | cat ~/.ssh/id_rsa.pub
git clone git@github.com:rbyelyy/bitstarter.git

# Navigate to bitstarter folder
cd bitstarter

# Create up to date development branch
git checkout development
git reset --hard origin/development

# Create up to date development branch
git checkout staging
git reset --hard origin/staging 

git checkout master

# Update Git config (adding username and email)
git config --global user.name rbyelyy
git config --global user.email rbyelyy@gmail.com

# Install npm
H=$(which npm)
if [[  "$H" != *npm* ]]
then
npm install
fi

# Update port in the web.js file
sed "s/5000/8080/" web.js

# Run web.js in the port 8080
#/usr/bin/env node web.js

# Check that local server is running on port 8080
#netstat -plnt|grep 8080

# Install Heroku
H=$(which heroku)

if [[  "$H" != *heroku* ]]
then
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
fi


# Login Heroku
heroku login
heroku keys:add
net=$(git branch -a)
if [[ "$net" != *staging-heroku*  ]]
then
heroku apps:create rbyelyy-bitstarter-s-mooc --remote staging-heroku
fi
if [[ "$net" != *production-heroku*  ]]
then
heroku apps:create rbyelyy-bitstarter-mooc --remote production-heroku
fi

# Push changes from Git master to Heroku production
git checkout master
git merge staging
git push production-heroku master:master

# Push changes from Git staging to Heroku staging
git checkout staging
git merge development
git push staging-heroku staging:master
