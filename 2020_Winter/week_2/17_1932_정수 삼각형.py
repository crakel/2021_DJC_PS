import sys

n = int(sys.stdin.readline())

t = []
res = []

for i in range(n, 0, -1): # 입력받은 수로 (n+1)(n+1)생성
    if i == n:
        t.append(list(map(int, '0' * ((2*n) + 1))))
    num = list(sys.stdin.readline().strip().split())
    tmp = []
    for j in range(len(num)): # 수 사이 공백에 0 넣어줌
        tmp.append(num[j])
        if j < len(num) - 1:
            tmp.append('0')

    t.append(list(map(int, i * ['0'] + tmp + i * ['0'])))

for i in range(1, n+1):
    for j in range(1, n*2):
        t[i][j] = t[i][j] + max(t[i-1][j-1], t[i-1][j+1])

print(max(t[-1]))
