#https://leetcode.com/problems/rotate-array/description/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a=k%len(nums)
        nums[:]=nums[-a:]+nums[:-a]
        return nums
