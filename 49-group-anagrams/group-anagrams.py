class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramset = {}
        for i in strs:
            sortedstr = "".join(sorted(i))
            if sortedstr in anagramset:
                anagramset[sortedstr].append(i)
            else:
                anagramset[sortedstr]=[i]
        return list(anagramset.values())