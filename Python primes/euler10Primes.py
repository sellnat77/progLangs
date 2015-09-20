import math

def is_prime( num ):
	if num < 2:
		return False
	
	if num == 2:
		return True
		
	if num % 2 == 0:
		return False
	
	for value in range(3,math.ceil(math.sqrt(num))):
		if num % value == 0 :
			return False
			
	return True
	
def get_primes( num ):
	for value in range(num,999999999):
		if is_prime(value):
			yield value
	
def sum_primes():

	sum = 0

	for val in get_primes(0):
		if (val >= 1999999999):
			break
		sum += val		
		
	return sum
		
    
#main
print(sum_primes())