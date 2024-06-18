# Brute force



from typing import List

def majorityElement(v: List[int]) -> List[int]:
    n = len(v) # size of the list
    ls = [] # list of answers

    for i in range(n):
        # selected element is v[i]:
        # Checking if v[i] is not already
        # a part of the answer:
        if len(ls) == 0 or ls[0] != v[i]:
            cnt = 0
            for j in range(n):
                # counting the frequency of v[i]
                if v[j] == v[i]:
                    cnt += 1

            # check if frquency is greater than n/3:
            if cnt > (n // 3):
                ls.append(v[i])

        if len(ls) == 2:
            break

    return ls


arr = [11, 33, 33, 11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()

# BETTER APPROACH(HASHING)




from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)


# OPTIMAL APPROACH(Extendded boyer moores voting algorithm)




from typing import List

def majorityElement(v: List[int]) -> List[int]:
    n = len(v) # size of the array

    cnt1, cnt2 = 0, 0 # counts
    el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

    # applying the Extended Boyer Moore’s Voting Algorithm:
    for i in range(n):
        if cnt1 == 0 and el2 != v[i]:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and el1 != v[i]:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ls = [] # list of answers

    # Manually check if the stored elements in
    # el1 and el2 are the majority elements:
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        if v[i] == el2:
            cnt2 += 1

    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)

    # Uncomment the following line
    # if it is told to sort the answer array:
    #ls.sort() #TC --> O(2*log2) ~ O(1);

    return ls

arr = [11, 33, 33, 11, 33, 11]
ans = majorityElement(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()





