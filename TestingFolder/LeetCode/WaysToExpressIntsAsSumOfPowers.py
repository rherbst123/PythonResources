n = 10
x = 2


MOD = 10 ** 9 + 7

dp = [[0] * (n +1) for _ in range(n + 1)]

dp[0][0] = 1


for i in range(1, n + 1):
    power = pow(i, x)
    for j in range(n + 1):
        dp[i][j] = dp[i-1][j]
        if power <= j:
            dp[i][j] = (dp[i][j] + dp[i-1][j-power]) % MOD
print(dp[n][n])