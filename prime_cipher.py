# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:17:36 2022

Prime-ception!

@author: A Ramsey
"""

def finds_stacked_powers_of_2(a, r, n):
    '''
    Parameters
    ----------
    a : int
        base number.
    r : int
        power of 2.
    n : int
        modulus.

    Returns
    -------
    to_sub : int
        a^(2^r) mod n.
    '''
    to_sub = a % n
    
    for R in range(1, r+1):
        to_sub = (to_sub * to_sub) % n
        
    return to_sub

def finds_powers_general(b, d, n):
    '''
    Parameters
    ----------
    b : int
        number you are raising to dth power
    d : int
        number you are raising b to the power of
    n : int
        modulo n

    Returns
    -------
    int
        b^d mod n
    '''
    bin_d = str(bin(int(d)))
    list_of_chars = []
    char_count = 0
    
    for char in bin_d:
        if char_count > 1:
            list_of_chars.append(int(char))
        char_count += 1
        
    list_of_chars.reverse()
    new_list = []
    
    for x in range(len(list_of_chars)):
        powers = list_of_chars[x]*(2**x)
        new_list.append(powers)
        
    mod_mul = 1
    new_count = 0
    
    for power in new_list:
        if power == 0:
            new_count +=1 
            continue
        mod = finds_stacked_powers_of_2(b, new_count, n)
        mod_mul*=mod
        new_count += 1
        
    return mod_mul % n

def finds_s(n):
    '''
    Parameters
    ----------
    n : int
        prime we're using

    Returns
    -------
    int
        s such that n = 2**s * d + 1
    '''
    for s in range(2, n + 1):
                if (n - 1) % (2**s) == 0:
                    continue
                
                else:
                    return (s - 1)

def better_prime_czecher(p):
    '''
    Parameters
    ----------
    p : int
        number you're checking to see if it's prime

    Returns
    -------
    bool
        True/False
    '''
    if p == 2 or p == 3:
        return True
    elif p % 2 == 0:
        return False
    if p == 1:
        return False
    
    witnesses = [2, 3]
    witness_count = 0
    
    for a in witnesses:
        bad_count = 0
        
        s = finds_s(p)
        d = (p-1)/(2**s)
        
        for r in reversed(range(s+1)): 
            b = finds_stacked_powers_of_2(a, r, p)
            
            if finds_powers_general(b, d, p) == 1:
                continue
            elif finds_powers_general(b, d, p) == p-1:
                witness_count += 1
                break
            else:
                bad_count += 1
                break
            
    if witness_count == 2:
        return True
    elif bad_count == 0:
        return True
    else:
        return False

def generates_prime_list(length):
    '''
    Parameters
    ----------
    length : int
        number of primes needed.

    Returns
    -------
    prime_list : list
        list of 'length' primes.
    '''
    prime_list = []
    count = 1
    
    #run through all numbers, checking if each is prime & adding if so until list is desired length
    while len(prime_list) < length:
        if better_prime_czecher(count):
            prime_list.append(count)
        
        count += 1
        
    return prime_list

def unit_counter(text, unit):
    '''
    Parameters
    ----------
    text : str
        text to count the number of units in.
    unit : str
        word, sentence or paragraph (use counter() for letter).

    Returns
    -------
    count : int
        number of units in text.
    '''
    count = 0
    
    #char: list of characters that indicate end of unit
    if unit == "word":
        char = [" "]
        #number of spaces = number of words - 1. same for paragraph breaks
        count += 1
        
    elif unit == "sentence":
        char = [".", "!", "?"]
        
    elif unit == "paragraph":
        char = ["\n"]
        count += 1
    
    else:
        return "unit must be word, sentence or paragraph. For letter, use counter()"
    
    for letter in text:
        if letter in char:
            count += 1
            
        else:
            continue
        
    return count
        

def counter(text, alphabet):
    '''
    Parameters
    ----------
    text : str
        text to count number of latin letters in.
    alphabet : list
        list of lowercase latin letters
        
    Returns
    -------
    count : int
        number of latin letters in text.
    '''
    count = 0
    
    for letter in text:
        if letter.lower() in alphabet:
            count += 1
            
        else:
            continue
    
    return count

def main(text, encrypt, unit):
    '''
    Parameters
    ----------
    encrypt : bool
        True if wanting to encrypt, False if wanting to decrypt.
    unit : str
        "letter" if en/decrypting by letter
        "word" if by word
        "sentence" if by sentence
        "paragraph" if by paragraph

    Returns
    -------
    new_text : str
        input encrypted or decrypted.
    '''
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    if unit == "letter":
        prime_list_o = generates_prime_list(counter(text, alphabet))
        
    else:
        prime_list_o = generates_prime_list(unit_counter(text, unit))
        
    prime_list = []
    
    if encrypt:
        for prime in prime_list_o:
            prime_list.append(prime % 26)
    else:
        #shift backwards for decryption
        for prime in prime_list_o:
            prime_list.append((26 - (prime % 26)) % 26)
        
    new_text = ""
    
    prime_count = 0
    text_count = 0
    
    for letter in text:
        letter = letter.lower()
        if letter.lower() in alphabet:
            new_alph_index = alphabet.index(letter) + prime_list[prime_count]
            
            if new_alph_index >= len(alphabet):
                new_alph_index = new_alph_index % 26
                
            new_text += alphabet[new_alph_index]
            
            if unit == "letter":
                prime_count += 1
                
            elif text_count == len(text) - 1:
                continue
            
            elif unit == "word":
                if text[text_count + 1] == " ":
                    prime_count += 1
            
            elif unit == "sentence":
                if text[text_count + 1] in [".", "!", "?"]:
                    prime_count += 1
                    
            elif unit == "paragraph":
                if text[text_count + 1] == "\n":
                    prime_count += 1
            
        else:
            new_text += letter
        
        text_count += 1
        
    return new_text

#text = input("text: ")
text = "the quick brown fox. Well, it jumps. over the lazy dog, that is? certainly."
e = "xml aiywg dzymh dqf. kuhl, kb zqqxc. clyt dvy lklq dsq, jzcx ug? cqhlwkrzs."

print(main(main(text, True, "word"), True, "letter"))
print(main(main(e, False, "letter"), False, "word"))