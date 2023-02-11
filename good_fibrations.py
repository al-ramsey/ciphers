# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 23:03:52 2022

@author: A Ramsey
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from random import randint
#!!!! test z_eight shifter
text = input("text to encode: ")
#alt_colours 26 = ["aquamarine", "mediumturquoise", "green", "olivedrab", "sienna", "darkgrey", "teal", "blue", "slateblue", "midnightblue", "indigo", "purple", "mediumorchid", "magenta", "violet", "deeppink", "crimson", "red", "salmon", "peru", "orange", "bisque", "khaki", "yellow", "greenyellow", "lime"]

def bounds(l):
    '''
    Parameters
    ----------
    l : list
        list of numbers (e.g points on graph).

    Returns
    -------
    bounds : list
        list of lists of adjacent numbers from l.
    '''
    bounds = []
    for element in l:
        if element != l[-1]:
            i = l.index(element)
            b_set = [element, l[i+1]]
            bounds.append(b_set)
            
    return bounds

def find(nested_list, char):
    '''
    Parameters
    ----------
    nested_list : list
        list of lists.
    char : any
        character which may be in a list in the nested list.
        
    Returns
    -------
    int, or None
        int = list index (if it is in one of the lists). None otherwise
    '''
    for l in nested_list:
        if char in l:
            return nested_list.index(l)
        
        else:
            continue

def colour_picker(colours, word_length):
    '''
    Parameters
    ----------
    colours : list
        list of colour keys in matplotlib.
    word_length : int
        length of word to be coloured.

    Returns
    -------
    colour_picks : list
        list of colours, one for each letter in word.
    '''
    c_length = len(colours)
    mod = math.floor(c_length/word_length)
    count = 0
    colour_picks = []
    
    while count < word_length:
        if count == word_length - 1:
            last_c_list = colours[mod*count:]
            y = randint(0, len(last_c_list) - 1)
            c = last_c_list[y]
        
        else:
            y = randint(0, mod - 1)
            c = (colours[mod*count:mod*(count+1)])[y]
            
        colour_picks.append(c)
        count += 1
        
    return colour_picks

def shifter(letter_list, shift_key):
    '''
    Parameters
    ----------
    letter_list : list
        list to be shifted.
    shift_key : int
        amount by which list will be shifted.

    Returns
    -------
    new_list : list
        shifted list.
    '''
    shift_key = shift_key % len(letter_list)
    count = 0
    new_list = []
    
    while count < len(letter_list):
        new_list.append(letter_list[(-1*shift_key)+count])
        count += 1
        
    return new_list

def crypt(text, z_eight):
    '''
    Parameters
    ----------
    text : str
        one word to be translated.
    z_eight : bool    
        True if shifting, False otherwise (for testing)

    Returns
    -------
    None. (plots graph)
    '''
    colours = ["aquamarine", "mediumturquoise", "green", "olivedrab", "teal", "blue", "midnightblue", "indigo", "purple", "mediumorchid", "magenta", "violet", "deeppink", "crimson", "red", "salmon", "peru", "orange", "bisque", "khaki", "yellow", "greenyellow", "lime"]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    p = np.pi
    repeat_count = [0]*26
    
    pre_bounds = [0, p/4, p/2, (3*p)/4, p, (5*p)/4, (3*p)/2, (7*p)/4, 2*p]
    letters = [["u", "m", "e"], ["v", "n", "f"], ["w", "o", "g"], ["x", "p", "h"], ["y", "q", "i"], ["r", "j", "b"], ["s", "k", "c"], ["t", "l", "d"]] #inner to outer
    
    rn = [1, 1.5, 2]
    our_bounds = bounds(pre_bounds)
    zipped = list(zip(our_bounds, letters))
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    
    count = 0
    
    for char in text:
        char = char.lower()
        
        if count != 0:
            if char in text[:count]:
                repeat_count[alphabet.index(char)] += 1
                
        if char not in alphabet:
            continue
        
        if char == "a" or char == "z":
            theta = np.linspace(0, 2*p, 1000)

            if char == "z":
                r = [0.5*(1+(0.08*(repeat_count[-1])))]*1000
                
            else:
                r = [0.1*(1+(0.5*(repeat_count[0])))]*1000
            
            ax.plot(theta, r, color = '%s'%(colour_picker(colours, len(text)))[count])
            count += 1
        
        else:
            tup = zipped[find(letters, char)]
            local_bounds = tup[0]
            local_lets = tup[1]
            
            if z_eight:
                local_lets = shifter(tup[1], count)
            
            theta = np.linspace(local_bounds[0]+p/8, local_bounds[1]+p/8, 1000)
            
            r_multiplier = rn[local_lets.index(char)]*(1+(0.05*(repeat_count[alphabet.index(char)])))
            r = r_multiplier*np.sin(4*(theta+(p/8)))
            ax.plot(theta, abs(r), color = '%s'%(colour_picker(colours, len(text)))[count])
            count += 1

    ax.set_rticks([0.5, 1, 1.5, 2])   #fewer radial ticks
    ax.set_rlabel_position(-22.5)  #move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("Hopf, my beloved <3", va='bottom')
    plt.show()
    
#crypt(text, False)
'''
def sentences(text, z_eight):

    words = text.split(" ")
    
    for word in words:
        crypt(word, z_eight)
        
        input("press enter")
        
sentences(text, False)
'''