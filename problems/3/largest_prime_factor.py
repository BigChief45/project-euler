### Jaime Alvarez - March 2016

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import random

def factors(n):
    # From:
    # http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def largest_prime_factor(factors):
    lpf = 0
    
    for i in factors:
        if MillerRabinPrimalityTest(i) and (i > lpf):
            #print i
            lpf = i
            
    return lpf
            
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
    
if __name__ == '__main__':
    n = 600851475143
    factors_list = factors(n)
    print "Largest Prime Factor = ", largest_prime_factor(factors_list)