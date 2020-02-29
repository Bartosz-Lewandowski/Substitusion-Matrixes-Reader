# Substitusion Matrixes Reader
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
## General info 
It's a programme that can read Substitusion Matrixes (PAM, BLOSUM, nucleotides). What is substitution matrix? In bioinformatics and evolutionary biology, a substitution matrix describes the rate at which one character in a sequence changes to other character states over time. Substitution matrices are usually seen in the context of amino acid or DNA sequence alignments, where the similarity between sequences depends on their divergence time and the substitution rates as represented in the matrix. [Wikipedia](https://en.wikipedia.org/wiki/Substitution_matrix).
Struggle was to made it universal for every record. Like for every delimiter used, or delete all comments and read only pure matrix as numpy array. I made it for college classes and it was a underlay for Needleman–Wunsch or Smith–Waterman algorithm.
## Technologies
* Python 3.7
* wxPython
* Numpy
