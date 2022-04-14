import sys

n = sys.stdin.readline()
f = int(sys.stdin.readline())
n = int(n[:-3] + '00')

for i in range(100):
    if (n+i) % f == 0:
        print("%02d" % i)
        break

