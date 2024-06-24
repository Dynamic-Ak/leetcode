#https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)  #typecast in string
        if x == x[ : :-1]: # reverse the string
            return True
        else:
            False
