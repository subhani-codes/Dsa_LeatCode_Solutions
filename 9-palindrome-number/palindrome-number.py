class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        s=0
        while n:
            r = n%10
            s = s*10+r
            n = n//10
        if s == x:
            return True
        else:
            return False

        