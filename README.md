# ciphers

Consists of 4 ciphers (made for fun):

1. cipher_greek: A substitution cipher with a twist: some common double letters in the english alphabet are substituted for a single Greek letter, and 'spare' Greek letters are randomly introduced (both of these are to try and minimise the possibility of brute force attacks; the assignments are based on what Greek letters are commonly assigned to physical/mathematical values e.g. a -> pi because pi is **A**rchimedes' constant)

2. dodecahedron: Each of the 12 faces of a dodecahedron is assigned a number, and each of its 30 edges (uniquely defined by the tuple of numbers corresponding to the faces bordering it) is assigned a letter/symbol. Then, the program moves through the elements of the group A5 (rotational symmetries of a dodecahedron) and the encoding of each letter becomes where it is mapped under this particular symmetry. After 60 symmetries, it resets.

3. good_fibrations: Takes in single words. Plots a graph: each letter of the alphabet has been assigned a point on a 2-sphere, then we look at its fibres (circles) under the Hopf Fibration (from the 'north' of the 3-sphere) - the polar graph is not entirely accurate, but gives a simple visualisation. Based on Samuel J. Li's visualisation: https://samuelj.li/hopf-fibration/. The colour indicated the order in which the letters are read.

4. prime_cipher: Runs through a list of prime numbers, Caeser shifts each letter by a prime modulo 26, changing prime every letter, word, sentence or paragraph (based on setting)
