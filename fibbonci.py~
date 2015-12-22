"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate"""

def fib(n):
	a=1
	b=1
	l=[]
	if int(n)==1:
		l.append(a)
	if int(n)==2:
		l.append(a)
		l.append(b)
	if int(n)>2:
		l.append(a)
		l.append(b)
		while int(n)>2:
			a=l[len(l)-2]
			b=l[len(l)-1]
			c=int(a)+int(b)
			l.append(c)
			n=int(n)-1
	return l
n=input("enter the nnumber of elements in the sequence:")
l=fib(n)
print(l)

