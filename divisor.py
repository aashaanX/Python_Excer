"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""


num=input("enter the number:")
num=int(num)
li=[]
for i in range(1,int(num+1)):
	i=int(i)
	if num%i == 0:
		li.append(i)
print(li)
	
