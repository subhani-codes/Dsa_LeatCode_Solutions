class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        total = 0
        freq = {0: 1}

        for num in nums:
            total += num

            if total - k in freq:
                count += freq[total - k]

            if total in freq:
                freq[total] += 1
            else:
                freq[total] = 1

        return count