# page 15
from typing import List

def nextGreaterPermutation(A: List[int]) -> List[int]:
    n = len(A) # size of the array.

    # Step 1: Find the break point:
    ind = -1 # break point
    for i in range(n-2, -1, -1):
        if A[i] < A[i + 1]:
            # index i is the break point
            ind = i
            break

    # If break point does not exist:
    if ind == -1:
        # reverse the whole array:
        A.reverse()
        return A

    # Step 2: Find the next greater element
    #         and swap it with arr[ind]:
    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break

    # Step 3: reverse the right half:
    A[ind+1:] = reversed(A[ind+1:])

    return A

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")
