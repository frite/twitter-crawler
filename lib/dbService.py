#!/usr/bin/env python
#
#   Copyright 2014 Frite M.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import peewee
import datetime
import time
import alertsClass

''' db initialization '''
database=""
szHost=""
username=""
password=""
'''Initialize Database Connection'''
mysql_db=peewee.MySQLDatabase(database,host=szHost,user=username,passwd=password)

dbFlag=0
global oTextColor
oTextColor=alertsClass.textAlert()
class MySQLModel(peewee.Model):
    """MySQL Peewee Model"""
    class Meta:
        database = mysql_db
        
class persons(MySQLModel):
	''' Class of users '''
	user_id = peewee.BigIntegerField(primary_key=True)
	screenname=peewee.TextField()
	name=peewee.TextField()
	description=peewee.TextField()
	listed_count=peewee.IntegerField()
	friends_count=peewee.IntegerField()
	statuses_count=peewee.IntegerField()
	followers_count=peewee.IntegerField()
	favorites_count=peewee.IntegerField()
	url=peewee.TextField()
	createdAt=peewee.DateTimeField()
	geo_enable=peewee.BooleanField()
	location=peewee.TextField()
	language=peewee.TextField()
	protected_profile=peewee.BooleanField()

class tweets(MySQLModel):
	''' Class of tweets '''
	tweet_id= peewee.BigIntegerField(primary_key=True)
	user_id = peewee.BigIntegerField()
	status=peewee.TextField()
	countFavorites=peewee.IntegerField()
	countRTs=peewee.IntegerField()
	time=peewee.DateTimeField()

class hashtags(MySQLModel):
	''' Class of hashtags '''
	hashtag = peewee.TextField()

class urls(MySQLModel):
	''' Class of URLs '''
	category_id= peewee.IntegerField()
	expanded_url=peewee.CharField()
	content=peewee.TextField()

class favorites(MySQLModel):
	''' Relationship of user-tweets '''
	user_id = peewee.BigIntegerField()
	tweet_id = peewee.BigIntegerField()

class followers(MySQLModel):
	''' Relationship of user-user '''
	user_id = peewee.BigIntegerField()
	follower_id = peewee.BigIntegerField()
	
class friends(MySQLModel):
	''' Relationship of user-user '''
	user_id = peewee.BigIntegerField()
	friend_id = peewee.BigIntegerField()
	
class retweets(MySQLModel):
	''' Relationship of user-tweets '''
	user_id = peewee.BigIntegerField()
	tweet_id = peewee.BigIntegerField()
	time=peewee.DateTimeField()
	
class tweetsHashes(MySQLModel):
	''' Relationship of tweets-hashtags '''
	hashtag_id=peewee.IntegerField()
	tweet_id=peewee.BigIntegerField()
	
class tweetsURLs(MySQLModel):
	''' Relationship of tweets-urls '''
	tweet_id=peewee.BigIntegerField()
	url_id=peewee.IntegerField()

def db_connect():
	''' Connect to db '''
	#print "Connecting to db"
	mysql_db.connect()

def db_close():
	''' db Disconnect '''
	#print "Killing connection"
	mysql_db.close()


def storeUser(userObject):
	''' Store user in db '''
	creationDay = userObject.created_at
	dbUser=persons(user_id=userObject.id,screenname=userObject.screen_name,name=userObject.name,description=userObject.description,listed_count=userObject.listed_count,friends_count=userObject.friends_count,statuses_count=userObject.statuses_count,followers_count=userObject.followers_count,favorites_count=userObject.favourites_count,url=userObject.url,geo_enable=userObject.geo_enabled,location=userObject.location,language=userObject.lang,protected_profile=userObject.protected,createdAt=creationDay)
	insert(dbUser,'An exception flew by while storing the user!')
def storeTweets(tweetObjects,userObject):
	''' Store tweet in db '''
	now=datetime.datetime.now()
	print ("\t[*]\tStoring %s's tweets. %s"%(userObject.screen_name,str(now)))
	for tweet in tweetObjects:
    		if hasattr(tweet, 'retweeted_status'):
			creationDay=tweet.retweeted_status.created_at
			dbTweet=tweets(tweet_id=tweet.retweeted_status.id,user_id=tweet.retweeted_status.user.id,status=tweet.retweeted_status.text,countFavorites=tweet.favorite_count,countRTs=tweet.retweet_count,time=tweet.retweeted_status.created_at)
			insert(dbTweet,'An exception flew by while storing the tweet (1)!')
			storeTweetEntities(tweet)
			storeRetweet(tweet.retweeted_status.id,userObject.id,tweet.created_at)
		else:
			creationDay=tweet.created_at
			dbTweet=tweets(tweet_id=tweet.id,user_id=tweet.user.id,status=tweet.text,countFavorites=tweet.favorite_count,countRTs=tweet.retweet_count,time=tweet.created_at)
			insert(dbTweet,'An exception flew by while storing the tweet (2)!')
			storeTweetEntities(tweet)
	now=datetime.datetime.now()
	print ("\t[*]\tFinished storing %s's tweets %s"%(userObject.screen_name,str(now)))
def storeRetweet(tweetID,UID,creationDay):
	dbRT=retweets(user_id=UID,tweet_id=tweetID,time=creationDay)
	insert(dbRT,'An exception flew by while storing the RT!')
	
def storeTweetEntities(tweet):
	''' Store tweet entities in db '''
        if hasattr(tweet,'entities'):
                storeHashtags(tweet)
                storeURLs(tweet)

def storeHashtags(tweet):
	''' Store hashtags in db '''
	if tweet.entities['hashtags'] is not None:
		for hashtag in tweet.entities['hashtags']:
			db_connect()
			dbHash=hashtags(hashtag=hashtag['text'])
			db_close()
			insert(dbHash,'An exception flew by while storing the hashtag!')
			storetweetsHashes(tweet.id,hashtag['text'])
			
def storeURLs(tweet):
	''' Store urls in db '''
	if tweet.entities['urls'] is not None:
		for url in tweet.entities['urls']:
			dbURL=urls(category_id= matchCategory(url['expanded_url']),expanded_url=url['expanded_url'],content=None)
			insert(dbURL,'An exception flew by while storing the url!')
			storetweetsURLs(tweet.id,url['expanded_url'])

def storeFollowers(followersObject,user):
	''' Store followers in db '''
	if(followersObject is None):
                return
	for follower in followersObject:
		dbFollower=followers(user_id=user.id,follower_id=follower)
		insert(dbFollower,'An exception flew by while storing the follower!')

def storeFriends(friendsObject,user):
	''' Store friends in db '''
	if(friendsObject is None):
                return
	for friend in friendsObject:
		dbFriend=friends(user_id=user.id,friend_id=friend)
		insert(dbFriend,'An exception flew by while storing the friend!')
		
def storeFavorites(userObject,favorites):
	''' Store favorites, requires authentication '''
	storeTweets(favorites)
	for favorite in favorites:
		dbFavorite=favorites(user = userObject.id, tweet =favorite.id)
		insert(dbFavorite,'An exception flew by while storing the favorite!')
		
def storetweetsHashes(tweetID,szhashtag):
	''' Relationship of tweets-hashtags '''
	db_connect()
	theHashtag=hashtags.get(hashtags.hashtag==szhashtag).id
	db_close()
	dbtweetHash=tweetsHashes(tweet_id=tweetID,hashtag_id=theHashtag)
	insert(dbtweetHash,'An exception flew by while storing the tweet Hashtag!')
	
def storetweetsURLs(tweetID,url):
	''' Relationship of tweets-urls '''
	db_connect()
	try:
		theURL=urls.get(urls.expanded_url==url).id
		db_close()
		dbtweetURL=tweetsURLs(tweet_id=tweetID,url_id=theURL)
		insert(dbtweetURL,'An exception flew by while storing the tweet URL!')
	except:
		exceptionPrint("Url not found")
		
def init():
	''' In first call, it'll create tables, or it will raise problems '''
	persons.create_table()
	tweets.create_table()
	hashtags.create_table()
	urls.create_table()
	favorites.create_table()
	followers.create_table()
	retweets.create_table()
	tweetsHashes.create_table()
	tweetsURLs.create_table()

def exceptionPrint(string,e=None):
	oTextColor.warning("\t[WARNING*]\t"+string)
	if e is not None:
		oTextColor.warning(str(e))

def matchCategory(url):
	''' Matches a category '''
	if url.find("facebook")!=-1:
		return 1
	elif url.find("youtube")!=-1 or url.find("youtu.be")!=-1:
		return 3
	elif url.find("blogspot")!=-1 or url.find("blogger")!=-1 or url.find("tumblr")!=-1 or url.find("wordpress")!=-1:
		return 2
	else:
		return 4
def insert(dbObject,alertText):
    db_connect()
    try:
		dbObject.save(force_insert=True)
		db_close()
    except Exception as e:
		exceptionPrint(alertText,e)
		db_close()



