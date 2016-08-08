### Jaime Alvarez - Apirl 2016

"""
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

import string
import sys

def generate_triangular_numbers():
    # Generates all triangular numbers up to n = 1000
    triangular_numbers = []
    for i in xrange(1, 1000 + 1):
        tn = int((1.00/2.00)*i*(i+1))
        triangular_numbers.append(tn)
        
    return triangular_numbers

if __name__ == '__main__':
    # Get all the words
    words = open('words.txt').read()
    
    # Split the words
    words = words.split(',')
    
    triangular_words_count = 0
    
    # First, generate our triangular numbers
    triangular_numbers = generate_triangular_numbers()
    
    for word in words:
        
        # Remove the double quotes
        word = word.replace('"', '')
        word_value = 0
        for letter in word:
            letter = letter.lower()
            
            # Get the letter's value
            index = string.lowercase.index(letter) + 1
            word_value += index
    
        # Check if it is a triangular word
        if word_value in triangular_numbers:
            triangular_words_count += 1
            
    print "Total # of Triangular Words: ", triangular_words_count