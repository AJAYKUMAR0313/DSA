# refer page 17
def bs(nums,n,c):
    def canweplace(nums,mid,n,c):
        cnt=1 
        last=nums[0]
        for i in range(1,len(nums)):
            if nums[i]-last>=mid:
                last=nums[i]
                cnt+=1 
        if cnt>=c:
            return True
        else:
            return False
    
    nums.sort()
    l=1
    h=nums[n-1]-nums[0]
    while(l<=h):
        mid=(l+h)//2
        if canweplace(nums,mid,n,c):
            l=mid+1
        else:
            h=mid-1 
    return h

for _ in range(int(input())):
    n,c=map(int,input().split())
    nums=[]
    for i in range(n):
        nums.append(int(input()))
    
    print(bs(nums,n,c))