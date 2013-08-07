#!/bin/sh
# $1 authorization key/pathto key
# This script helps to make access vi ssh to remote host more easier
# First parameter is a key name which you are using for accessing to remote host via ssh.
# Scrip create .ssh folder if necessary and create config file with proper content for accesss to host
cd ~/.ssh
if [ $? -eq 0 ]
then
mkdir -p ~/.ssh
fi

# Create bootstarter folder
cd $HOME/bootstarter/
if [ $? -eq 0 ]
then
mkdir -p $HOME/bootstarter/
fi

# Copy key to SSH
cat ~/.ssh/$1
if [ $? -eq 0 ]
then
echo XXX
else
cp $HOME/bootstarter/cs184-rbyelyy-stanford-edu.pem ~/.ssh/
fi

# Set proper permissions for key and SSH folder
chmod 400 ~/.ssh/$1
chmod 700 ~/.ssh

# Creating config file for easy login to AWS instance
touch ~/.ssh/config
echo Host aws > ~/.ssh/config
echo HostName ec2-54-213-1-128.us-west-2.compute.amazonaws.com >> ~/.ssh/config
echo User ubuntu >> ~/.ssh/config
echo IdentityFile "~/.ssh/"$1 >> ~/.ssh/config
