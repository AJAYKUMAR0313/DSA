# refer page 17

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def find(idx, target, subset):
            if target == 0:
                res.append(subset[:])
                return  # Terminate this branch

            if target < 0 or idx == len(candidates):
                return  # Terminate this branch

            # Include current candidate
            subset.append(candidates[idx])
            find(idx, target - candidates[idx], subset)
            subset.pop()  # Backtrack

            # Skip current candidate
            find(idx + 1, target, subset)

        find(0, target, [])
        return res