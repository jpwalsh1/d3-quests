#!/usr/bin/env python

import urllib2, json
import datetime

bnet = raw_input('Enter your Bnet ID, ex. Name#1234: ')
region = raw_input('Enter your region. us/eu/kr: ')
char_filter = raw_input('Filter by character name(leave empty for all characters): ')
bnet = bnet.replace('#', '-')

acts = ['act1', 'act2', 'act3', 'act4', 'act5']
act1 = ['The Fallen Star', 'The Legacy of Cain', 'A Shattered Crown', 'Reign of the Black King', 'Sword of the Stranger', 'The Broken Blade', 'The Doom in Wortham', 'Trailing the Coven', 'The Imprisoned Angel', 'Return to New Tristram']
act2 = ['Shadows in the Desert', 'The Road to Alcarnus', 'City of Blood', 'A Royal Audience', 'Unexpected Allies', 'Betrayer of the Horadrim', 'Blood and Sand', 'The Black Soulstone', 'The Scouring of Caldeum', 'Lord of Lies']
act3 = ['The Siege of Bastion\'s Keep', 'Turning the Tide', 'The Breached Keep', 'Tremors in the Stone', 'Machines of War', 'Siegebreaker', 'Heart of Sin']
act4 = ['Fall of the High Heavens', 'The Light of Hope', 'Beneath the Spire', 'Prime Evil']
act5 = ['The Fall of Westmarch', 'Souls of the Dead', 'The Harbinger', 'The Witch', 'The Pandemonium Gate', 'The Battlefields of Eternity', 'Breaching the Fortress', 'Angel of Death']

def getChars (bnet):
        url = 'http://' + region + '.battle.net/api/d3/profile/' + bnet + '/'

        response = urllib2.urlopen(url)
        json_profile = json.load(response)

        characters = [] 
        print 'Last Updated:'
        print datetime.datetime.fromtimestamp(int(json_profile['lastUpdated'])).strftime('%Y-%m-%d %H:%M:%S') 
              
        for char in json_profile["heroes"]:
                if char_filter:
                        if char_filter.lower() != char['name'].lower():
                                continue
                characters.append(char['id'])

        return characters


def checkQuests (characters):

        for character in characters:
                url = 'http://' + region + '.battle.net/api/d3/profile/' + bnet + '/hero/' + str(character)
                response = urllib2.urlopen(url)
                json_char = json.load(response)

                for act in acts:
                        completed = []
                        exec('total_quests = len(' + str(act) + ')')
                        if len(json_char['progression'][act]['completedQuests']) < total_quests and json_char['level'] == 70:
                                print '\n{0} - {1} - Level {2} - {3}'.format(json_char['name'], json_char['class'], json_char['level'], act)
                                for quest in json_char['progression'][act]['completedQuests']:
                                        completed.append(str(quest['name']))

                                exec('missing = set(' + str(act) + ') - set(completed)')
                                for q in missing:
                                        print q

checkQuests(getChars(bnet))
