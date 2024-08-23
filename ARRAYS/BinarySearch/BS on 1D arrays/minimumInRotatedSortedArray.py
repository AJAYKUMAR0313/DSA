import sys
def findMin(arr: [int]):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        # search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
            
        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half

        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)


# SImplified Solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        while l < h:
            mid = (l + h) // 2
            
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        
        return nums[l]
