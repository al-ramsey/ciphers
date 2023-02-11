# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:50:43 2022

@author: A Ramsey
"""

file = input("file: ")
filein = open(file, "r", encoding="utf-8")
to_translate = filein.readlines()
filein.close()

new = input("to create: ")
newin = open(new, "w", encoding="utf-8")

#rotations: f=face centred (1 number), v=vertex centred (3 numbers), e=edge centred (2 numbers)
#note: if low memory/high time, change lists to tuples

e = []
f1 = [[2, 4, 6, 5, 3], [7, 8, 10, 11, 9]]
f2 = [[1, 3, 7, 8, 4], [5, 9, 12, 10, 6]]
f3 = [[1, 5, 9, 7, 2], [4, 6, 11, 12, 8]]
f4 = [[1, 2, 8, 10, 6], [3, 7, 12, 11, 5]]
f5 = [[1, 6, 11, 9, 3], [2, 4, 10, 12, 7]]
f6 = [[1, 4, 10, 11, 5], [2, 8, 12, 9, 3]]

v123 = [[1, 3, 2], [4, 5, 7], [6, 9, 8], [10, 11, 12]]
v124 = [[1, 2, 4], [3, 8, 6], [5, 7, 10], [9, 12, 11]]
v135 = [[1, 5, 3], [2, 6, 9], [4, 11, 7], [8, 10, 12]]
v146 = [[1, 4, 6], [2, 10, 5], [3, 8, 11], [7, 12, 9]]
v156 = [[1, 6, 5], [2, 10, 9], [3, 4, 11], [7, 8, 12]]
v237 = [[1, 9, 8], [2, 3, 7], [4, 5, 12], [6, 11, 10]]
v248 = [[1, 7, 10], [2, 8, 4], [3, 12, 6], [5, 9, 11]]
v278 = [[1, 9, 10], [2, 7, 8], [3, 12, 4], [5, 11, 6]]
v359 = [[1, 11, 7], [2, 6, 12], [3, 5, 9], [4, 10, 8]]
v379 = [[1, 11, 8], [2, 5, 12], [3, 9, 7], [4, 6, 10]]

e12 = [[1, 2], [3, 4], [5, 8], [6, 7], [9, 10], [11, 12]]
e13 = [[1, 3], [2, 5], [4, 9], [6, 7], [8, 11], [10, 12]]
e14 = [[1, 4], [2, 6], [3, 10], [5, 8], [7, 11], [9, 12]]
e15 = [[1, 5], [2, 11], [3, 6], [4, 9], [7, 10], [8, 12]]
e16 = [[1, 6], [2, 11], [3, 10], [4, 5], [7, 12], [8, 9]]
e23 = [[1, 7], [2, 3], [4, 9], [5, 8], [6, 12], [10, 11]]
e24 = [[1, 8], [2, 4], [3, 10], [5, 12], [6, 7], [9, 11]]
e27 = [[1, 12], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11]]
e28 = [[1, 12], [2, 8], [3, 10], [4, 7], [5, 11], [6, 9]]
e35 = [[1, 9], [2, 11], [3, 5], [4, 12], [6, 7], [8, 10]]
e37 = [[1, 12], [2, 9], [3, 7], [4, 11], [5, 8], [6, 10]]
e39 = [[1, 12], [2, 11], [3, 9], [4, 10], [5, 7], [6, 8]]
e46 = [[1, 10], [2, 11], [3, 12], [4, 6], [5, 8], [7, 9]]
e48 = [[1, 12], [2, 10], [3, 11], [4, 8], [5, 9], [6, 7]]
e56 = [[1, 11], [2, 12], [3, 10], [4, 9], [5, 6], [7, 8]]

translations = [e, f1, f2, f3, f4, f5, f6, v123, v124, v135, v146, v156, v237, v248, v278, v359, v379, e12, e13, e14, e15, e16, e23, e24, e27, e28, e35, e37, e39, e46, e48, e56]
full_t = []

for t in translations:
    full_t.append(t)
    count = 0
    
    if len(t) == 2:
        while count < 3:
            full_t.append((t, count+2))
            count += 1
            
    elif len(t) == 4:
        while count < 1:
            full_t.append((t, count+2))
            count += 1

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ".", ",", "?"]
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 7), (2, 8), (3, 5), (3, 7), (3, 9), (4, 6), (4, 8), (4, 10), (5, 6), (5, 9), (5, 11), (6, 10), (6, 11), (7, 8), (7, 9), (7, 12), (8, 10), (8, 12), (9, 11), (9, 12), (10, 11), (10, 12), (11, 12)]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

decoding = True

def finds_decoder_degree(base, degree):
    '''
    Parameters
    ----------
    base : list
        base rotation 'g'.
    degree : int
        number of times 'g' is performed (power g is raised to).

    Returns
    -------
    int
        degree needed to perform action in reverse.
    '''
    if len(base) == 2:
        return (5 - degree)
    elif len(base) == 4:
        return (3 - degree)
    else:
        return degree

def dodecahedron(to_translate, decoding):
    '''
    Parameters
    ----------
    to_translate : list
        list of lines of document to be translated.
    decoding : bool
        True if decrypting, False if encrypting.

    Returns
    -------
    None.
    '''
    new_string = ""
    count = 0
    
    for line in to_translate:
        for char in line:
            char = char.lower()
            if char not in letters:
                if char in numbers:
                    new_string += char
                    continue
                #new_string += char
                continue
            
            rotation = full_t[count]
            edge = edges[letters.index(char)]
            
            if isinstance(rotation, tuple): #if tuple
                base = rotation[0] #base rotation g
                degree = rotation[1] #number of rotations
                if decoding:
                    degree = finds_decoder_degree(base, degree)
                
            else:
                base = rotation
                degree = 1
                if decoding:
                    if base == []:
                        degree = 1
                    else:
                        degree = finds_decoder_degree(base, degree)
    
            for n in range(degree):
                new_es = []
                edge_count = [0, 0]
                
                if base == []:
                    new_letter = char #identity e
                    
                for r in base: #cycle in rotation
                    for e in edge: #face in edge tuple               
                        if e in r: #if face changed under rotation
                            if r[-1] == e:
                                new_e = r[0]
                                
                            else:
                                new_e = r[r.index(e) + 1] #what face changed to
    
                            new_es.append(new_e) #add to list of edges
                            edge_count[edge.index(e)] = 1
            
                if base != []:
                    for c in edge_count:
                        if c == 0:
                            new_es.append(edge[edge_count.index(c)])
    
                    new_es.sort()
                    new_es = tuple(new_es) #list to edge tuple - n/a for identity
                    edge = new_es 
                    
                new_letter = letters[edges.index(edge)] #change edge tuple to corresponding letter
    
            new_string += new_letter
            count += 1
            if count >= 60:
                count -= 60
                
        newin.write(new_string)
        #newin.write("\n")
        new_string = ""
    
    newin.close()

dodecahedron(to_translate, False)
