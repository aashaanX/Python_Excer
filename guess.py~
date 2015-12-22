"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right."""

from random import randint

num=randint(1,9)
count=0
ch=''
while ch!='exit':
	user=input("guess number:")
	count+=1
	if num==int(user):
		print("Exactly rit")
		ch=input("type exit to stop guessing or click any to continue:")
		continue
	elif num>int(user):
		print("guessed low")
		ch=input("type exit to stop guessing or click any to continue:")
		continue
	else:
		print("guessed high")
		ch=input("type exit to stop guessing or click any to continue:")
		continue
print("took "+str(count)+" chances to guess")
