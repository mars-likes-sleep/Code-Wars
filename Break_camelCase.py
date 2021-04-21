"""
Complete the solution so that the function will break up camel casing,
 using a space between words.
"""

def solution(s):
    current_slice = 0
    last_slice = 0
    word_bank = []
    for letter in s:
        if letter == letter.upper():
            word_bank.append(s[last_slice:current_slice])
            last_slice = current_slice
        current_slice += 1
    word_bank.append(s[last_slice:current_slice])
    
    broken_up = " ".join(word_bank)
    
    return broken_up

"""

Optimal code
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

"""

