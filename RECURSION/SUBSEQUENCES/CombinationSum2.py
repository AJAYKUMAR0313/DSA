class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        ds=[]
        def recursion(index,target,ds):
            if target==0:
                res.append(ds[:])
                return
            for i in range(index,len(candidates)):
                if(i>index and candidates[i]==candidates[i-1]):#1st elemet is to be picked so i>index shld continue
                    continue
                if target<candidates[i]:
                    break
                ds.append(candidates[i])
                recursion(i+1,target-candidates[i],ds)
                ds.pop()
        candidates.sort()
        recursion(0,target,[])
        return res
    
    