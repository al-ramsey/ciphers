# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:17:36 2022

Prime-ception!

@author: A Ramsey
"""

from functions import better_prime_czecher

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