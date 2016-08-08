### Jaime Alvarez - March 2016

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



if __name__ == '__main__':
    product = 0

    # Dickson's Method:
    # https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson.27s_method
    # r^2 = 2 x s x t
    
    
    # Use a starting r = 2 value, then increase by 2 to keep r an even integer
    for r in xrange(6, 100000, 2):
        print "r = %s" % r
        print "======="
        a,b,c = 0,0,0
        
        # r squared
        r2 = r**2
        
        # Find all factor pairs of (r^2)/2
        # First get all the factors
        all_factors = factors(r2/2)
        factor_pairs = []
        
        # Get pairs that their product is equal to r2
        for i in all_factors:
            for k in all_factors:
                if (i * k == r2/2) and ([k, i] not in factor_pairs):
                    # Found a pair
                    factor_pairs.append([i,k])
        
        #print factor_pairs
        
        # Use the factor pairs to generate the triples
        # x = r + s     y = r + t       z = r + s + t
        for pair in factor_pairs:
            s = pair[0]
            t = pair[1]
            
            # Find the triple values
            x = r + s
            y = r + t
            z = r + s + t
            
            triple_sum = x + y + z
            
            # Print the triple
            print "[%s, %s, %s] ::: %s + %s + %s = %s" % (x, y, z, x, y, z, triple_sum)
            
            # Check if the sum of the triple
            if triple_sum == 1000:
                # We found the triple, get the product
                product = x * y * z
                print "abc = %s" % product
                break