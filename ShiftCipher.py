#Shift Cipher:

def shift_cipher(text,key):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    textLowerCase = list(text.lower())
    
    for i in range(0,len(textLowerCase)):
        replacement = (ALPHABET.index(textLowerCase[i])+key+26)%26
        textLowerCase[i] = ALPHABET[replacement]
        
    return "".join(textLowerCase)

#Test Cases:
print(shift_cipher('HELLO',2)) #'jgnnq'
print(shift_cipher('JGNNQ',-2)) #'hello'
print(shift_cipher('ZDQABCVN',1)) #'bfscdexp'
print(shift_cipher('abcdefg',2)) #'jgnnq'
print(shift_cipher('abcdefghijklmnopqrstuvwxyz',2))
print(shift_cipher('abcdefghijklmnopqrstuvwxyz',-2)) 

