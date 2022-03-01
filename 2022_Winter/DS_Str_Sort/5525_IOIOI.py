import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

count = 0
ioi_count = 0
i = 1

while i < m - 1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        ioi_count += 1
        if ioi_count == n:
            count += 1
            ioi_count -= 1
        i += 1
    else:
        ioi_count = 0
    i += 1

print(count)

# 시간 초과?
# def is_ioi(s, n):
#     I_count = 0
#     O_count = 0
#
#     for i in range(2*n+1):
#         if i % 2 == 0 and s[i]=='I':
#             I_count += 1
#         else:
#             if s[i] == 'O':
#                 O_count += 1
#
#     if O_count == n and I_count == n+1:
#         return True
#
#     else:
#         return False
#
#
# count = 0
# for i in range(m):
#     if i <= m-(2*n+1):
#         if is_ioi(s[i:], n):
#             count += 1
#
# print(count)