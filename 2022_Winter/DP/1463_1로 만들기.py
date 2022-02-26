import sys

x = int(sys.stdin.readline())
dp = {1: 0}


def make_one(num):
    for i in range(2, num+1):
        if i % 3 == 0:
            if i % 2 == 0:
                dp[i] = min(dp[i//3] + 1, dp[i//2]+1, dp[i - 1] + 1)
            else:
                dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1

        # 이하 코드로 3가지 case 모두 판별 가능
        # d[i] = d[i - 1] + 1
        # if i % 3 == 0:
        #     d[i] = min(d[i], d[i // 3] + 1)
        #     1을 더하는 것은 d는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다. d[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문이다.
        # if i % 2 == 0
        #     d[i] = min(d[i], d[i // 2] + 1)


make_one(x)
print(dp.popitem()[1])