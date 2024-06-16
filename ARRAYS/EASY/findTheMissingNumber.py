#refer Page no.4
#BRUTE FORCE APPROACH



def missing_number(a, N):
    # Outer loop that runs from 1 to N:
    for i in range(1, N + 1):
        # flag variable to check if an element exists
        flag = 0

        # Search the element using linear search:
        for j in range(len(a)):
            if a[j] == i:
                # i is present in the array:
                flag = 1
                break

        # check if the element is missing (i.e., flag == 0):
        if flag == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


#BETTER APPROACH (USING HASHING)




def missingNumber(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


#OPTIMAL APPROACH(USING SUMMATION)




def missingNumber(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


#OPTIMAL APPROACH 2(UING XOR)



def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()


