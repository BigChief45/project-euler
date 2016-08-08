# Method 1: Two-Parameter Generator Set
# When m and n are any two positive integers (m < n):
# a = n^2 - m^2
# b = 2nm
# c = n^2 + m^2
m = 1
n = 2
a,b,c = 0,0,0

product = 0

# We are going to create triples until a set of triples a + b + c = 1000 is satisfied.
while (a + b + c) <= 1000:
    # Generate triple
    a = (n**2) - (m**2)
    b = 2*n*m
    c = (n**2) + (m**2)

    print "(%s, %s, %s)" % (a,b,c)

    m += 1
    n += 1

# Check if our triple sums to 1000
if (a + b + c) == 1000:
    # Once the triple has been found, let's get the product
    print "Triple Found: (%s, %s, %s" % (a,b,c)
    product = a * b * c
else:
    print "Triple not found, using Method #2..."
    
    # Triple was not found, we must use a different method
    a = 3
    b = 4
    c = 5
    n = 2
    while (a + b + c) <= 1000:
        a *= n
        b *= n
        c *= n
        print "(%s, %s, %s)" % (a,b,c)    
        #n += 1

# Check if the triple sums to 1000
if (a + b + c) == 1000:
    print "Triple Found: (%s, %s, %s" % (a,b,c)
    product = a * b * c