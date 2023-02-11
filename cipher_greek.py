# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:09:59 2022

@author: A Ramsey
"""
from random import randint


eng_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "gr", "fi", "ri", "re", "st", "an", "in", "or"]
reserve_alpha = ["p", "m", "CH", "r", "l", "n", "f", "k", "IN", "d", "g", "F", "s", "a", "t", "PSL", "z", "e", "TH", "O", "ET", "PSU", "E"] #deprecated
frequency_latin_alphabet = ["1", "c", "e", "2", "i", "k", "3", "o", "q", "s", "u", "w", "y", "b", "4", "f", "h", "5", "l", "n", "p", "r", "t", "v", "x", "z", "a", "d", "g", "j", "m"] #deprecated - for testing for brute force attacks
alphabet = ["\u03C0", "\u03BC", "\u03C7", "\u03C1", "\u03BB", "\u03BD", "\u03C6", "\u03BA", "\u03F5", "\u03B4", "\u03B3", "\u03A6", "\u03C3", "\u03B1", "\u03C4", "\u03C8", "\u03B6", "\u03B5", "\u03B8", "\u03C9", "\u03B7", "\u03A8", "\u0395", "\u03D5", "\u03D1", "\u03BE", "\u0393", "\u03B2", "\u03D6", "\u03B9", "\u0398"]
spares = ["\u03BF", "\u03C5"]

input_file = input("to translate: ")
filein = open(input_file, "r")
lines = filein.readlines()
filein.close()
new_lines = ""
czech = False #True if skipping next character (if double letter), False otherwise

for line in lines:
    count = 0 #keeps count of character index
    line = line.lower()
    newline = ""
    
    for char in line:
        if czech:
            czech = False
            count += 1
            continue #skip next character and reset czech
        
        if count != len(line) - 1: #if not last characater
            if char + line[count + 1] in eng_alphabet:
                char = alphabet[eng_alphabet.index(char + line[count + 1])]
                czech = True #char = double letter and set czech
                
            elif char in eng_alphabet:
                #char = frequency_latin_alphabet[eng_alphabet.index(char)] - test
                char = alphabet[eng_alphabet.index(char)]
                
        elif char in eng_alphabet:
            char = alphabet[eng_alphabet.index(char)]
            
        y = randint(1, 7)
        
        if y == 3 and line[count] in eng_alphabet:
            newline = newline + char + spares[randint(0, 1)] #add in random spare
            #newline = newline + char + frequency_latin_alphabet[randint(0, 4)+26] - test
        
        else:
            newline = newline + char #for non-letters (leave alone)
            
        count += 1
    new_lines = new_lines + newline
'''
new = input("to create: ")
newin = open(new, "w")
newin.write(new_lines)
newin.close()
'''
#print(lines) - test
print(new_lines)