# refer page 18

# BRUTE FORCE(LINEAR SEARCH)

def linearSearch(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    n = len(a)  # size of array
    longest = 1
    # pick an element and search for its consecutive numbers
    for i in range(n):
        x = a[i]
        cnt = 1
        # search for consecutive numbers using linear search
        while linearSearch(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)



# BETTER APPROACH(USING SORTING)

def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    # sort the array
    a.sort()
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1

    # find longest sequence
    for i in range(n):
        if a[i] - 1 == lastSmaller:
            # a[i] is the next element of the
            # current sequence
            cnt += 1
            lastSmaller = a[i]
        elif a[i] != lastSmaller:
            cnt = 1
            lastSmaller = a[i]
        longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)


# OPTIMAL APPROACH(USE SET DATA STRUCTURE)



def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)


