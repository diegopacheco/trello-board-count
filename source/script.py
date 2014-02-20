#!/usr/bin/python2.7
from trollop import TrelloConnection
from auth import *

import sys

print 'Extracting pending Code Reviews per projets. \n'
trello = TrelloConnection(CONSUMER_KEY, authenticate()['oauth_token'])

total_pending = 0
sys.stdout.write( '## Pending Code Review: \n' )
for board in filter(lambda b: b.name.lower() in BOARDS, trello.me.boards):
	sys.stdout.write( board.name + ':')
	allcards = filter(lambda l: l.name.lower() in LISTS, board.lists)

	if allcards != []:
		for l in allcards:
			sys.stdout.write( ' ' + str(len(l.cards)) + '\n' )
			total_pending = total_pending + len(l.cards)
	else:
		sys.stdout.write(' 0\n')
print '## Total Pending Code Review: %i' % total_pending