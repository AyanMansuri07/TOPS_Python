""" 
A
BC
DEF
GHIJ
"""

k=65
for row in range(6):
    for col in range(1,row+1):
        print(chr(k),end=" ")
    print()