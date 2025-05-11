With String:
------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        rev=s[::-1]
        if(s==rev):
            return True
        else:
            return False

Without String:
---------------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        original = x

        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10

        return original == rev

