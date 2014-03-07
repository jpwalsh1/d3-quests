#!/usr/bin/env python

import urllib2, json

bnet = raw_input('Enter your Bnet ID, ex. Name#1234: ')
bnet = bnet.replace('#', '-')
 
def getChars (bnet):
	url = 'http://us.battle.net/api/d3/profile/' + bnet + '/'
        
	response = urllib2.urlopen(url)
	json_profile = json.load(response)
	
	characters = []
	for char in json_profile["heroes"]:
		characters.append(char['id'])
		 
	return characters
 
 
def checkQuests (characters):
	act1 = ['The Fallen Star', 'The Legacy of Cain', 'A Shattered Crown', 'Reign of the Black King', 'Sword of the Stranger', 'The Broken Blade', 'The Doom in Wortham', 'Trailing the Coven', 'The Imprisoned Angel', 'Return to New Tristram']

	for character in characters:
		url = 'http://us.battle.net/api/d3/profile/' + bnet + '/hero/' + str(character)
 		response = urllib2.urlopen(url)
		json_char = json.load(response)
		
		if len(json_char['progress']['normal']['act1']['completedQuests']) < 10 and json_char['level'] == 60:
			print '{0} - {1} - Level {2}'.format(json_char['name'], json_char['class'], json_char['level'])
			completed = []
			for quest in json_char['progress']['normal']['act1']['completedQuests']:
				completed.append(str(quest['name']))
			
			missing = set(act1) - set(completed)
			for q in missing: print q	
 
checkQuests(getChars(bnet))
