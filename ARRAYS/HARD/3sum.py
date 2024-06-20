# BruteForce
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if not A:
            return -1
        
        cnt1, cnt2, el1, el2 = 0, 0, None, None

        # First pass to find potential candidates
        for num in A:
            if el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                el1, cnt1 = num, 1
            elif cnt2 == 0:
                el2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # Second pass to count actual occurrences of candidates
        cnt1, cnt2 = 0, 0
        for num in A:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        n = len(A)
        result = []
        if cnt1 > n // 3:
            result.append(el1)
        if cnt2 > n // 3:
            result.append(el2)
        
        if result:
            return result[0]  # Return any number that appears more than n/3 times
        return -1

# Example usage
sol = Solution()
print(sol.repeatedNumber((1000441, 1000441, 1000994)))  # Output: 1000441
print(sol.repeatedNumber((3, 3, 4, 2, 4, 4, 2, 4, 4)))  # Output: 4
print(sol.repeatedNumber((1, 2, 3, 1, 1)))  # Output: 1
print(sol.repeatedNumber)

# BETTER APPROACH(SET)




def triplet(n, arr):
    st = set()

    for i in range(n):
        hashset = set()
        for j in range(i + 1, n):
            # Calculate the 3rd element:
            third = -(arr[i] + arr[j])

            # Find the element in the set:
            if third in hashset:
                temp = [arr[i], arr[j], third]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])

    # store the set in the answer:
    ans = list(st)
    return ans


arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print()

# OPTIMAL APPROACH




def triplet(n, arr):
    ans = []
    arr.sort()
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans


arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(n, arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print()





