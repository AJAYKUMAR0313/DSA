class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        while (l<=h):
            mid=(l+h)//2
            # print(mid,self.isok(weights,mid,days))
            if self.isok(weights,mid,days)<=days:
                h=mid-1
            else:
                l=mid+1
        return l

    def isok(self,weights,capacity,days):
        days=1
        load=0
        for i in range(len(weights)):
            if (load+weights[i])>capacity:
                load=weights[i]
                days+=1
            else:
                load+=weights[i]
        return days


        