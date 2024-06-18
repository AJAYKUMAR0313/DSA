# Variation 1

import math

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = pascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")
    

# Variation 2 (Naive Approach)


import math

def nCr(n, r):
    res = 1
    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    # printing the entire row n:
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end=" ")
    print()

if __name__ == "__main__":
    n = 5
    pascalTriangle(n)
    

# Variartion 2 (Optimal approach)

def pascalTriangle(n):
    ans = 1
    print(ans, end=" ") # printing 1st element

    #Printing the rest of the part:
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

if __name__ == "__main__":
    n = 5
    pascalTriangle(n)


# Variation 3(Naive approach)

from typing import *

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()

#  Variation 3 (Optimal approach)


from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
