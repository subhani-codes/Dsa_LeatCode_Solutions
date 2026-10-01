class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in t:
                return False
            if s.count(i) != t.count(i):  # Changed "i" to i
                return False
            
        return True