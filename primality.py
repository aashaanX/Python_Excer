"""Ask the user for a number and determine whether the number is prime or not"""

num=input("enter a number:")

def prime(num):
	count=0
	for i in range(2,int(num)):
		if int(num)%int(i) == 0:
			count+=1
	if count==0:
		print("number is prime")
	else:
		print("number is not a prime number")
prime(num)
		
