# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[c]=nums[i]
                c+=1
        return c    
