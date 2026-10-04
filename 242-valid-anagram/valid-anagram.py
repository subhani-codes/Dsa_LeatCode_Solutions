class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            pack = [0] * 26 
            for i in s:
                pack[ord(i) - ord('a')] += 1
            for i in t:
                pack[ord(i) - ord('a')] -= 1
            for i in range(len(pack)):
                if pack[i] != 0:
                    return False
        return True
