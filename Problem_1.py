#projecteuler.net - Problem 1
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.
#
#Answer - 233168
#

def Multiples(upper_limit):
	lst = [False] * upper_limit
	sum = 0
	index_three = 2
	index_five = 4
	
	while(index_three < upper_limit):
		lst[index_three] = True
		index_three += 3
	while(index_five < upper_limit):
		lst[index_five] = True
		index_five += 5
	
	for y in range(upper_limit):
	    if(lst[y] == True):
		    sum += y+1
	
	return(sum)
	
print(Multiples(999))
