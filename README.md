twitter-crawler
===============
Description
---------------
My M.Sc. Thesis was a project regarding insider's threat, Twitter and some other things.
The Project was called Euphemia, part of which is the crawler. 
This is a stripped-down version of the crawler developed for the needs of the thesis.

Requirements
---------------
Python 2.7
MySQL >5 (In the future this is going to change though)

Python requirements
-------------------
Most of the requirements are available through pip.
tweepy (pip install tweepy)
python-mysql (pip install python-mysql)
peewee  (pip install peewee)

How to use
-----------
You'll be setting up a mysql database.
Import the sql file included in this project.
Although the lib/dbService.py file has a function to 
create the tables I wouldn't advice you to to do so.
Set the values for lib/dbService.py (host, user, paswd etc).

Set the values for lib/twitterService.py (



cKey=*consumer_key*



cSecret: *consumer_password*



atKey: *access_key*



atSecret=*access_secret*


szName=*screen_name_of_your_account*



Use it as you wish.
Fork it, hack it, expand it, destroy it. 
