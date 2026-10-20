import random
class Solution:
    def quicksort(self, arr: list[int], start: int, end: int):
        if start >= end:
            return
        
        t = random.randint(start,end)
        arr[start],arr[t] = arr[t],arr[start]
        p = start 
        i = start+1
        j = end
        
        while True:
            while i <= end and arr[i] <= arr[p]:
                i += 1
            while j >= start and arr[j] > arr[p]:
                j -= 1
            
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
                
        arr[j], arr[p] = arr[p], arr[j]
        self.quicksort(arr, start, j - 1)
        self.quicksort(arr, j + 1, end)

    def sortColors(self, nums: list[int]) -> None:
        i, j, p = 0, len(nums) - 1, 0
        self.quicksort(nums, i, j)