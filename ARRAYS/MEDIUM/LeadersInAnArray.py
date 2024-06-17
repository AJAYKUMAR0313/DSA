# REFER PAGE 16 AND 17


def printLeaders(arr, n):
    ans = []
  
    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans

# Main function
if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end=" ")

    print()


# ex:
# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > m:
                m,arr[i] = arr[i],m
            else:
                arr[i] = m
        return arr
