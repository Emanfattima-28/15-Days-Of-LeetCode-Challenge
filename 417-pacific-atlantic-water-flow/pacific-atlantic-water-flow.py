class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        for i in range(m):
            dfs(i, 0, pacific)       
        for j in range(n):
            dfs(0, j, pacific)     
        for i in range(m):
            dfs(i, n-1, atlantic)  
        for j in range(n):
            dfs(m-1, j, atlantic)     
        result = [[r, c] for (r, c) in pacific & atlantic]
        return result
        