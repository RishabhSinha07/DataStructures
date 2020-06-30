def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1] * m for _ in range(n)]
    for x in range(1, len(dp)):
        for y in range(1, len(dp[x])):
            dp[x][y] = int(dp[x - 1][y]) + int(dp[x][y - 1])
    return dp[n - 1][m - 1]
