class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        mpp = [-1] * 256


        left = 0
        right = 0
        n = len(s)
        length = 0
        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)


            mpp[ord(s[right])] = right


            length = max(length, right - left + 1)
            right += 1
        return length


if __name__ == "__main__":
    str = "takeUforward"
    obj = Solution()
    print("The length of the longest substring without repeating characters is",
          obj.lengthofLongestSubstring(str))