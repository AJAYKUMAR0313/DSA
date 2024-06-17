# refer page 22
from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)

