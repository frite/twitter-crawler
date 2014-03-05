#!/usr/bin/python
# -*- coding: utf-8 -*-
alphabet=['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']
keywords=['greek','greece','ellada','athens'] #'el' gives too many false positives:/

for letter in alphabet:
	''' turn everything into UTF-8 '''
	alphabet2=letter.decode("utf-8")
	
def greekUser(userObject):
	''' User is greek based on its profile info '''
	userAttrsList=[unicode(userObject.description.lower()),unicode(userObject.name.lower()),unicode(userObject.lang.lower()),unicode(userObject.location.lower())]
	for letter in alphabet2:
		if any(unicode(letter) in unicode(userAttr) for userAttr in userAttrsList):
			return True
	for keyword in keywords:
		if any(keyword in unicode(userAttr) for userAttr in userAttrsList):
			return True
	return False

def greekTweets(tweetsObjectList):
	''' User is greek based on its tweets '''
	for letter in alphabet2:
		if any(unicode(letter) in unicode(tweetStatus.text.lower()) for tweetStatus in tweetsObjectList):
			return True
	return False
