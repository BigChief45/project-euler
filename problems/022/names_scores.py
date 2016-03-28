### Jaime Alvarez - March 2016

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


import string

# Open the file and insert the names into the array
names_line = open("names.txt").readline()
alphabet = string.ascii_uppercase

# Remove the ""s
names_line = names_line.replace('"', "")

# Get each name separated by a comma into the array
names = names_line.split(",")

## Sort the list
names.sort()

total_score = 0

for name in names:
    # Calculate the score
    
    # Calculate the position of the name in the sorted list
    position = names.index(name) + 1
    
    # Calculate the worth, compare to 'alphabet' list
    worth = 0
    for letter in name:
        worth += alphabet.index(letter) + 1
    
    score = position * worth
    
    total_score += score
    #print "%s\t%s\t\t%s\t%s" % (position, name, worth, score)

print "Total score = ", total_score