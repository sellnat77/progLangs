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
	primes = []
	
	for value in range(0,num):
		if is_prime(value):
			primes.append(value)
			
	return primes
	
def sum_primes():
	return 0
    
#main
print(is_prime(4))
print(get_primes(100))