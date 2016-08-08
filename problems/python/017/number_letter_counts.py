### Jaime Alvarez - March 2016

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

# Install inflect with: pip install inflect
import inflect

number_words = {}

number_words[1] = 'one'
number_words[2] = 'two'
number_words[3] = 'three'
number_words[4] = 'four'
number_words[5] = 'five'
number_words[6] = 'six'
number_words[7] = 'seven'
number_words[8] = 'eight'
number_words[9] = 'nine'
number_words[10] = 'ten'
number_words[11] = 'eleven'
number_words[12] = 'twelve'
number_words[13] = 'thirteen'
number_words[14] = 'fourteen'
number_words[15] = 'fifteen'
number_words[16] = 'sixteen'
number_words[17] = 'seventeen'
number_words[18] = 'eighteen'
number_words[19] = 'nineteen'
number_words[20] = 'twenty'
number_words[30] = 'thirty'
number_words[40] = 'forty'
number_words[50] = 'fifty'
number_words[60] = 'sixty'
number_words[70] = 'seventy'
number_words[80] = 'eighty'
number_words[90] = 'ninety'


n = 1000
inflect_engine = inflect.engine()
letter_count = 0

for i in xrange(1, n+1):
    number_to_word = str(inflect_engine.number_to_words(i))
    letter_count += len(number_to_word.replace('-', '').replace(' ', ''))

print "Total # of Letters: ", letter_count

# Backup algorithm method
def num_to_wor(i):
    try:
        word = number_words[i]
    except KeyError:
        try:
            # Tenths
            word = number_words[i-i%10] + '-' + number_words[i%10].lower()
        except KeyError:
            try:
                # Hundreds
                hundred = int(i / 100)
                word = number_words[hundred] + ' hundred and ' + number_words[(i-100)-(i-100)%10] + number_words[(i-100)%10].lower()
            except KeyError:
                try:
                    # Thousands
                    pass
                except KeyError:
                    print 'Number out of range'
    
    # Remove the hyphens and spaces, then count the number of letters
    letters = len(word.replace('-', '').replace(' ', ''))
    letter_count += letters
    
    print "%s : %s" % (word, letters)
    
    return i