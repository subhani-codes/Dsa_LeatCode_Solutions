class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
       
        n = len(nums)
        k %= n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return nums
