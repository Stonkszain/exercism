import string

def is_pangram(sentence):
# Iteration 1
    
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # sentence = sentence.lower()
    # for i in alphabet:
    #     if i not in sentence:
    #         return False
    # return True

# Iteration 2
    
    # sentence = sentence.lower()
    # letters = set()
    
    # for i in sentence:
    #     if i.isalpha():
    #         letters.add(i)
            
    # if len(letters) == 26:
    #     return True
    # return False

# Iteration 3

    return set(string.ascii_lowercase).issubset(sentence.lower())

    # pass
