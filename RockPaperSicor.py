"""Make a two-player Rock-Paper-Scissors game."""

import os

ch='y'
while ch=='y':
	player1=input("Player 1/enter value 1.rock 2.paper 3.siccor :")
	os.system('clear')
	player2=input("Player 2/enter value 1.rock 2.paper 3.siccor :")
	os.system('clear')
	if player1==player2:
		print("same")
		ch=input("\nclick y if you want to continue:")
		continue
	if player1=='1':
		if player2=='2':
			print("player2 won")
		else:
			print("player1 won")
		ch=input("\nclick y if you want to continue:")
		continue
	if player1=='2':
		if player2=='3':
			print("player2 won")
		else:
			print("player1 won")
		ch=input("\nclick y if you want to continue:")
		continue
	if player1=='3':
		if player2=='1':
			print("player2 won")
		else:
			print("player1 won")
		ch=input("\nclick y if you want to continue:")
		continue








