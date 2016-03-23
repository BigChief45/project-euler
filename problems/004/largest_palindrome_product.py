### Jaime Alvarez - March 2016

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPalindrome(num):
    # Determines if the number is a palindrome
    num = str(num)
    
    # First, check if length is even
    if len(num) % 2 != 0:
        return False
        
    firstpart, secondpart = num[::2], num[1::2]
    
    # If first half is equal to the 2nd half inverted, return true
    if (firstpart == secondpart[::-1]):
        return True
    else:
        return False

if __name__ == '__main__':
    digit_start = 100
    digit_end = 999
    largest_palindrome = 0
    
    for i in range(digit_start, digit_end + 1):
        for k in range(digit_start, digit_end + 1):
            if isPalindrome(i * k) and ((i * k) > largest_palindrome):
                largest_palindrome = i * k
                
    print "Largest Palindrome = ", largest_palindrome