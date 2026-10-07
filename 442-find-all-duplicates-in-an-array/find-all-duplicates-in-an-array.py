class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
       
        dup = []
        for num in nums:
            index = abs(num) - 1  # Fixed: changed 'numb' to 'num'
            if nums[index] < 0:
                dup.append(abs(num))
            else:
                nums[index] = -nums[index]
        return dup