class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1=len(nums1)
        m1=len(nums2)
        if n==0:
            return nums1
        if m1==0:
            nums1[0]=nums2[0]
            return nums1
        
        j=0
        for i in range (m,n1):
            nums1[i]=nums2[j]
            j+=1
        print(nums1.sort())

        
