def search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid
        # Edge case (if there are duplicates):(Rotated Sorted array 2)
        # if arr[low] == arr[mid] and arr[mid] == arr[high]:
        #     low += 1
        #     high -= 1
        #     continue    
        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)