class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        container ={}
        for i in nums:
            if i in container:
                container[i]+=1
            else:
                container[i]=1
            if container[i]> n/2:
                return i
        