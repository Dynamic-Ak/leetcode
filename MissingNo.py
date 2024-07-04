#https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)+1
        for i in range(l):
            if i in nums:
                None
            else:
                return i
