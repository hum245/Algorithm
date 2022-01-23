n = list(map(int, input()))
l = len(n)

if n[0] == 0:
    print(0)
    exit()
else:
    n = [0] + n

    dp = [0] * (l+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, l+1):
        if n[i] > 0:
            dp[i] += dp[i-1]
        if (n[i-1]*10 + n[i]) >= 10 and (n[i-1]*10 + n[i]) <= 26:
            dp[i] += dp[i-2]

    print(dp[l] % 1000000)

    