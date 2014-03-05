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

# Use this if you want explicitly greek users.

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
