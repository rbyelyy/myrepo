#! /bin/sh
git --version
if [ "$?" != "0" ]
then 
  echo "git is not installed properly."
fi
files=`ls -la|grep .git`
echo $files
if [[ "$files" == *.git* ]] 
then
  echo "Yes"
else
 git config --global user.name "Roman Byelyy"
 git config --global user.email "rbyelyy@gmail.com"  
 git init
 git status
fi	
git remote add origin git@github.com:rbyelyy/myrepo.git
# Generating rsa keys and adding them into github
if [$1 == "rsa_yes"]
then
  ssh-keygen -t rsa -C "rbyelyy@gmail.com"
fi
ssh -T git@github.com
git push -u origin master
