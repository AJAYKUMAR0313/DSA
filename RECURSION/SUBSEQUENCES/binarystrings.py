def All_Binary_Strings(arr,num,r):

    if(r == num):

        for i in range(num):
            print(arr[i],end="")
        print(end=" ")
        return
    
    elif(arr[r-1]):

        arr[r] = 0
        All_Binary_Strings(arr, num, r + 1)

    else:
    
        arr[r] = 0
        All_Binary_Strings(arr,num,r+1)
        arr[r] = 1
        All_Binary_Strings(arr,num,r+1)


def Print(a,num):
    a[0] = 0
    All_Binary_Strings(a,num,1)
    a[0] = 1
    All_Binary_Strings(a,num,1)


# driver's code

n = 2
a = [False for i in range(n)]
Print(a,n)
