def solution(s):
    slice_pos = 0
    last_slice = 0
    add_string = " "
    word_bank = []
    for letter in s:
        if letter == letter.upper():
            word_bank.append(s[last_slice:slice_pos])
            last_slice = slice_pos
        slice_pos += 1
    word_bank.append(s[last_slice:slice_pos])
    
    broken = " ".join(word_bank)
    
    return broken
    

test_case = "helloWorld"

print(solution(test_case))

"""

Optimal code
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

"""
