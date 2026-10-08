class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_occurrence = {0: -1} 
        running_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in first_occurrence:
              
                max_length = max(max_length, i - first_occurrence[running_sum])
            else:
                
                first_occurrence[running_sum] = i

        return max_length