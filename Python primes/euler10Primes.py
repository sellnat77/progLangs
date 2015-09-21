import math

#Target value to find sum
target = 2e6

def is_prime( num ):
	"Returns whether or not a value is prime"
	if num < 2:
		return False
	
	if num == 2:
		return True
		
	if num % 2 == 0:
		return False
	#If num can be divided by any number between 3- ciel(sqrt(num+1))
	#then it is not a prime number
	for value in range(3,math.ceil(math.sqrt(num+1))):
		if num % value == 0 :
			return False
			
	return True
	
def get_primes( num ):
	"Yields all prime numbers from num-target"
	for value in range(num,int(target)):
		if is_prime(value):
			yield value
	
def sum_primes():
	"Adds all the results from get_primes starting from 0"
	sum = 0

	for val in get_primes(0):
		if (val > target):
			break
		sum += val		
		
	return sum
		
#main
print("The sum is: ",sum_primes())



