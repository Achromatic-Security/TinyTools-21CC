#Cards 2-6 have a value of +1.
#Cards 7-9 have no value.
#Cards worth 10 have a value of -1.
#Aces also have a value of -1.
import math
from random import randint
import time

cards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}

cardArray = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
draw = []

# adding suit tracking later for extra sanity checking for re-suffle/multideck games.
heartcards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}
clubscards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}
diamondscards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}
spadescards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}

suit = 0
decks = 1.0

def fillDraw():
	global decks
	global cardArray
	global cards
	global draw
	totalCards = 13 * decks * 4
	print 'shuffling ' + str(totalCards) + ' cards'
	i = 0
	while i <= int(totalCards):
		k = randint(0,12)
		if cards['c' + cardArray[k]] < (4 * int(decks)):
			draw.append(cardArray[k])
			cards['c' + cardArray[k]] += 1 
			i += 1
			if i == 52:
				i += 1
	cards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}

def currentCount():
	global cards
	global decks
	global baseDecks
	global tempBaseDecks
	startCount = 0
	for k, v in cards.iteritems():
		if k in ['c2','c3','c4','c5','c6']:
			startCount += v
		elif k in ['c7','c8','c9']:
			startCount = startCount
		elif k in ['c10','cj','cq','ck','ca']:
			startCount -= v
		if v > 4:
			suspectedDecks = math.ceil(v / 4.0)
			if suspectedDecks > float(decks):
				decks = suspectedDecks
	if decks > tempBaseDecks:
		print "DECK SIZE INCREASED DUE TO CARD COUNT"
		tempBaseDecks = decks
	return startCount / decks

def addCard(c):
	global cards
	global decks
	global baseDecks
	if c == 'r':
		if raw_input('are you sure you want to reset the count? [y/N]:') == 'y':
			cards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}
			print 'count reset \n\n'
			decks = baseDecks
			
		else:
			print 'reset cancelled\n'
	elif c == 'exit':
		if raw_input('are you sure you want to quit? [y/N]:') == 'y':
			exit()
	elif c == 'd':
		if raw_input('are you sure you want to override the deck count? [y/N]:') == 'y':
			baseDecks = float(raw_input('Enter the number of decks you think there is in the shoe:'))
			decks = baseDecks
	else:
		if 'c' + c in cards:
			cards['c' + c] += 1
			print '.' * cards['c' + c]
				#print 'reshuffle/multi-deck warning. You have recorded '+ str(cards['c' + c]) + ' ' + c + '\'s meaning this tool may not work as expected (or it\'s time for a counter reset).'
		else:
			print 'invalid input. Values are: a 2 3 4 5 6 7 8 9 10 j q k\n'

print """
 _______  __    _______  _______     _______          
/ ___   )/  \  (  ____ \(  ____ \   (  ____ )|\     /|
\/   )  |\/) ) | (    \/| (    \/   | (    )|( \   / )
    /   )  | | | |      | |         | (____)| \ (_) / 
  _/   /   | | | |      | |         |  _____)  \   /  
 /   _/    | | | |      | |         | (         ) (   
(   (__/\__) (_| (____/\| (____/\ _ | )         | |   
\_______/\____/(_______/(_______/(_)|/          \_/   
                                                      


Simple card counter for Blackjack (21)

If the count is +2 or above you have a better chance of winning!

Possible input values: 

a 2 3 4 5 6 7 8 9 10 j q k
type 'r' and hit enter to reset the counter
type 'exit' and hit enter to quit the tool

Good Luck.

"""
selectmode = raw_input('Enter the mode you wish to use: [live/sim/practice]')
if selectmode.lower() == 'live':
	mode = 1
elif selectmode.lower() == 'sim':
	mode = 2
elif selectmode.lower() == 'practice':
	dificulty = int(raw_input('select difficulty: [1/2/3]'))
	mode = 3
else:
	print "you had one job. mode not recognised. defaulting to Live"
	mode = 1



baseDecks = float(raw_input('Enter the number of decks there is in the shoe (or your best guess):'))
decks = baseDecks
tempBaseDecks = decks

if mode == 3:
	fillDraw()
	i = 0
	for val in draw:
		if dificulty == 3:
			time.sleep(1)
		if dificulty == 2:
			time.sleep(2)
		if dificulty == 1:
			temp = raw_input('Hit Enter for the next card (or q to exit)')
			if temp == 'q':
				exit()
		addCard(val)
		print 'Drew a ' + val
		i +=1
		if i == 10:
			temp = raw_input('Hit Enter to reveal the count so far!')
			print '---------------------------------------\n\ncurrent count is: ' + str(currentCount()) + ' \n\n---------------------------------------'
			temp = raw_input('Hit Enter for the next round (or q to exit) ')
			if temp == 'q':
				exit()
			i = 0

if mode == 2:
	fillDraw()
	for val in draw:
		addCard(val)
		print 'Drew a ' + val
		print 'current count is: ' + str(currentCount())
	print "Done. the final value should be 0.0"
elif mode == 1:
	while 1:
		print 'current count is: ' + str(currentCount())
		print 'decks: ' + str(decks)
		addCard(str(raw_input('enter card:')))