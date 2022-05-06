import sys
n = int(sys.stdin.readline())
list = []

for _ in range(n):
    list.append(int(sys.stdin.readline()))

for x in sorted(list):
    print(x)

# Merge sort 시간초과.. (append?)
# import sys
#
# def merge_sort(list):
#     if len(list) <= 1:
#         return list
#
#     mid = len(list) // 2
#     left = merge_sort(list[:mid])
#     right = merge_sort(list[mid:])
#
#     return merge(left, right)
#
# def merge(left, right):
#     res = []
#     while len(left) > 0 or len (right) >0:
#         if len(left) > 0 and len(right) >0: # 왼쪽 오른쪽 모두 남은 경우
#             # 왼쪽 오른쪽중 큰 수를 추가하고 리스트 슬라이싱
#             if left[0] <= right[0]:
#                 res.append(left[0]) #append를 써서 그런듯
#                 left = left[1:]
#
#             else:
#                 res.append(right[0])
#                 right = right[1:]
#
#         elif len(left) > 0: # 왼쪽만 남은 경우
#             res.append(left[0])
#             left = left[1:]
#
#         elif len(right) > 0: # 오른쪽만 남은 경우
#             res.append(right[0])
#             right = right[1:]
#     return res
#
# n = int(sys.stdin.readline())
# list = []
#
# for _ in range(n):
#     list.append(int(sys.stdin.readline()))
#
# for x in merge_sort(list):
#     sys.stdout.write('{}\n'.format(x))


# 퀵정렬 사용시 시간초과..
# import sys
# sys.setrecursionlimit(100000)
#
# def quick_sort(list, start, end):
#     if start >= end:
#         return
#
#     pivot = list[(start + end) // 2]
#     left = start
#     right = end
#
#     while left <= right: #pivot 기준으로 이동시키면서 작은값은 왼쪽, 큰값은 오른쪽에 정렬
#         while list[left] < pivot:
#             left += 1
#         while list[right] > pivot:
#             right -= 1
#         if (left <= right):
#             #list[left], list[right] = list[right], list[left]
#             temp = list[left]
#             list[left] = list[right]
#             list[right] = temp
#             left+=1
#             right-=1
#
#     quick_sort(list, start, right)
#     quick_sort(list, left, end)
#
# n = int(sys.stdin.readline())
# list = []
#
# for _ in range(n):
#     list.append(int(sys.stdin.readline()))
#
# quick_sort(list, 0, n-1)
# for x in list:
#     print(x)