### Jaime Alvarez - April 2016

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

import collections
import random

def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    ''' first we want to express n as : 2^s * r ( were r is odd ) '''
    
    ''' the odd part of the number '''
    oddPartOfNumber = number - 1
    
    ''' The number of time that the number is divided by two '''
    timesTwoDividNumber = 0
    
    ''' while r is even divid by 2 to find the odd part '''
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 
     
    '''
    since there are number that are cases of "strong liar" we 
    need to check more then one number
    '''
    for time in range(3):
        
        ''' choose "Good" random number '''
        while True:
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        ''' randomNumberWithPower = randomNumber^oddPartOfNumber mod number '''
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        
        ''' if random number is not 1 and not -1 ( in mod n ) '''
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            ''' while we can squre the number and the squered number is not -1 mod number'''
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                ''' squre the number '''
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1
            '''     
            if x != -1 mod number then it because we did not found strong witnesses
            hence 1 have more then two roots in mod n ==>
            n is composite ==> return false for primality
            '''
            if (randomNumberWithPower != (number - 1)):
                return False
            
    ''' well the number pass the tests ==> it is probably prime ==> return true for primality '''
    return True 
    
def rotate(l,n):
    return l[n:] + l[:n]


if __name__ == '__main__':
    
    circular_primes_count = 0
    
    for i in xrange(1, 1000000+1):
        is_circular_prime = True
        
        # First, check if the number itself is prime
        if not MillerRabinPrimalityTest(i):
            continue
        
        # If it's prime, we continue to check for the rotations
        
        # The original number represented as a list of digits
        number = collections.deque(str(i))
        
        for k in xrange(0, len(str(i))):
            number.rotate(1)
            #print ''.join(list(number))
            
            # Check if it's prime
            if not MillerRabinPrimalityTest(int(''.join(list(number)))):
                is_circular_prime = False
                break
        
        if is_circular_prime:
            #print "%s is a circular prime" % i
            circular_primes_count += 1
            
    print "Total circular primes = ", circular_primes_count