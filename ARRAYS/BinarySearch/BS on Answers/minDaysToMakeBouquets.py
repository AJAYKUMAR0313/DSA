class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        l=min(bloomDay)
        h=max(bloomDay)
        while (l<=h):
            mid=(l+h)//2
            if self.possibleBouquets(bloomDay,mid,m,k)>=m:
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
    def possibleBouquets(self,nums,mid,m,k):
        cnt=0
        numOfBou=0
        for i in nums:
            if i<=mid:
                cnt+=1
            else:
                numOfBou+=(cnt//k)
                cnt=0
        numOfBou+=(cnt//k)
        return numOfBou