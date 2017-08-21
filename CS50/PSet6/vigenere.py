import sys

def main():
    """
    Vigenere cipher. Two modes: decipher and cipher. 
    Takes two console arguments: key and mode.
    Two possible modes: cipher and decipher.
    """
    
    argv = sys.argv
    argc = len(argv)
    keys = list()
    mode = argv[2]
    
    if argc != 3:
        print("Usage: python3 vigenere <key> <mode(cipher-decipher)>")
        
    if mode == "decipher":
        text = input("ciphertext: ")
    else:
        text = input("plaintext: ")
        
    for i in range(len(argv[1])):
        if ord('A') <= ord(argv[1][i]) <= ord('Z'):
            keys.append(ord(argv[1][i]) - ord('A'))
        else:
            keys.append(ord(argv[1][i]) - ord('a'))
    
    j = 0
    output = ""
    for i in range(len(text)):
        if j >= len(keys):
            j = 0
        key = keys[j]
        if not text[i].isalpha():
            output += text[i]
            continue
        rotated_char = rotate(text[i], key, mode)
        output += chr(rotated_char)
        j += 1
    
    if mode == "decipher":
        print("plaintext: {}".format(output))  
    else:
        print("ciphertext: {}".format(output)) 
    exit(0)        


def rotate(letter, key, mode):
    """
    Rotates a character forwards if in "cipher" mode,
    backwards if in "decipher" mode, key times.
    """
    
    if mode == "cipher":
        inc = 1
    else:
        inc = -1
    increment = (key % 26)
    if (ord('a') <= ord(letter) <= ord('z')):
        beginning = ord('a')
        end = ord('z')
    else:
        beginning = ord('A')
        end = ord('Z')
    
    alpha_index = ord(letter) - beginning
    
    mult = 1
    if mode == "decipher" and increment > 12:
        increment = 26 - increment
        mult = -1 
        
    for i in range(increment):
        if (alpha_index >= (end - beginning)):
            alpha_index = 0
        else:
            alpha_index += inc * mult
   
    return alpha_index + beginning 
             
    
main()
