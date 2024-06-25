#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        s2 = ''.join(char for char in s1 if char.isalnum())
        if s2 == s2[::-1]:
            return True
        else:
            return False

'''
# s1 is the original string
s1 = "YourOriginalStringHere!"

# Create an empty list to store the valid characters
valid_chars = []

# Loop through each character in s1
for char in s1:
    # Check if the character is a letter or number
    if char.isalnum():
        # If it is, add it to the list of valid characters
        valid_chars.append(char)

# Join the list of valid characters into a new string
s2 = ''.join(valid_chars)

# Print the result
print(s2)
'''
