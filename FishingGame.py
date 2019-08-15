# This is a fishing game 1.0

import random
import math

print('\nHey there, this is a fishing game. Basically you need to cast to get fish. You get 20 cast before you day finishes. \n')

name = input("\nPlease enter your name: ")
castcnt = 20
castnum = 20
castres = 0
monay = 0
day = 0

#When you cast you have a chance to catch a variety of fish.... or nothing at all. Each type of fish has a standard value and obviously the more rare the fish the higher the value')

#Setting values in dictionary form for "Price of fish" (POF) of fish for rare to common: Snapper, Blue Cod, Red Cod, Grouper, Monk Fish, Kawaii, Sand Shark.

POF = {'Snapper':30.00, 'BlueCod':25.00, 'RedCod':20.00, 'Grouper':15.00, 'MonkFish':10.00, 'Kawaii':5.00, 'SandShark':2.00, 'Stingray':1.20}

# Nedding to add a random number regenertor

while castnum > 0:
	print('\nYou have ' + str(castnum) + ' casts left!')
	wc = input("\nPlease enter c and press enter to cast: ")
	if wc == 'c':
		print('\nCasting')
	else:
		print('\nYOU SUCK!')
		break
	
	cast = random.randint(1,1000)

	castnum = castnum - 1

	if 0 > cast <= 10:
		castres = castres + (POF['Snapper'])
		print('\nYou got a SNAPPER!!')
	elif 11 > cast <= 50:
		castres = castres + (POF['BlueCod'])
		print('\nYou got a BLUECOD!!')
	elif 51 > cast <= 150:
		castres = castres + (POF['RedCod'])
		print('\nYou got a REDCOD!!')
	elif 151 > cast <= 300:
		castres = castres + (POF['Grouper'])
		print('\nYou got a GROUPER!!')
	elif 301 > cast <= 500:
		castres = castres + (POF['MonkFish'])
		print('\nYou got a MONKFISH!!')
	elif 501 > cast <= 750:
		castres = castres + (POF['SandShark'])
		print('\nYou got a SANDSHARK!!')
	elif 751 > cast <= 950:
		castres = castres + (POF['Stingray'])
		print('\nYou got a STINGRAY!!')
	else:
		print('\nYou caught NOTHING!!')
		

print('\nGame over ' + name + ', you made ' + str(castres) + ' dollars!')


