from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        container = {}

        for i in nums:
            if i in container:
                container[i] += 1
            else:
                container[i] = 1

        sortcontainer = sorted(
            container.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [sortcontainer[i][0] for i in range(k)]