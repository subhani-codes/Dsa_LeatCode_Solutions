class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        mymap = {}
        n = len(nums)
        for i in nums:
            mymap[i] = mymap.get(i, 0) + 1
            
        return sorted([k for k,v in mymap.items() if v > n//3])