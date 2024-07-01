#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/1306215453/
class Solution:
    def check(self, nums: List[int]) -> bool:
        gaddari = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%len(nums)]:
                gaddari += 1
        if gaddari > 1:
            return False
        else:
            return True
