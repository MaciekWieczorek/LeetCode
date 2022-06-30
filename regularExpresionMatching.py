import string

def isMatch(s, p):
        
        alfabet = list(string.ascii_lowercase)
        regular_def = {".": alfabet,
                       "*": alfabet}
        
        
        match = True
        if "." not in p and "*" not in p:
            if s != p:
                return False
                
        for letter_idx, letter in enumerate(s):
            if letter not in alfabet:
                print(letter)

print(isMatch("aa", ".*"))