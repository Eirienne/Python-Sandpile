# Author : WindSeer and Morbyx

import numpy as np
import os

# x = np.random.randint(9, size=(3,3))

# Clear terminal
clear = lambda: os.system('cls')

# Max sandpile per block
maxPile = 4

clear()
print("Sandpile Python Simple")

# Input Custom Matrix
# arr = input("Input Matrix [ , = for new column And ; for new row] :")

# Set Default matrix w/o input
# arr = "0,0,0;0,16,0;0,0,0"

# To check matrix string
# print(arr)

# Create matrix from string
# x = np.matrix(arr)


# Custom row and column
row = (input("Input Row: "))
while(row == "" or int(row) <= 0):
    row = (input("Please Input Row:"))
col = (input("Input Column:"))
while(col == "" or int(col) <= 0):
    col = (input("Please Input Column:"))

sandPile = np.zeros([int(row),int(col)], dtype=int)

# To check matrix size
# print(row, col)

i = (int(row)-1)/2
j = (int(col)-1)/2
sandPile[int(i)][int(j)] = int(input("First pile : ")) #Insert first pile

# Set temporary matrix
temp = sandPile

# Statement for continuously create matrix
powerOn = True

# Matrix creation
while powerOn:

    # Print Matrix
    print(temp)

    # When value in matrix >= maxPile, that block value got subtract with maxPile
    temp = np.where(temp>=maxPile, temp-maxPile, temp)

    # Topple sandpile
    mask = (sandPile >= maxPile)

    temp[:, :-1] += mask[:, 1:] # topple left
    temp[:, 1:] += mask[:, :-1] # topple right
    temp[:-1, :] += mask[1:, :] # topple up
    temp[1:, :] += mask[:-1, :] # topple down

    # Check if there's no more to topple
    COMPARISON = sandPile == temp
    CHECK_EQUAL = COMPARISON.all()

    sandPile = temp
    
    if CHECK_EQUAL == powerOn:
        powerOn = False
        print("Shutting Down...")