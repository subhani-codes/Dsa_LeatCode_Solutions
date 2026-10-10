class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        count = maxcount = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                count += 1
                if maxcount < count:
                    maxcount = count
            else:
                count = 1
        return maxcount