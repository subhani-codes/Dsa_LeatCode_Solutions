class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out of bounds or water cell
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return
            
            # Mark the land cell as visited/sink it
            grid[r][c] = 0
            
            # Traverse all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # 1. DFS from all boundary land cells
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and grid[r][c] == 1:
                    dfs(r, c)
                    
        # 2. Count remaining land cells that cannot reach the boundary
        enclave_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    enclave_count += 1
                    
        return enclave_count