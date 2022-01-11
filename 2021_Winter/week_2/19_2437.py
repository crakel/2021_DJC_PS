n = int(input())

a = list(map(int, input().split()))

def MIN(list):
    min = float('inf')
    for i in range(len(list)):
        if 0 <= list[i] < min:
            min = list[i]
    return min

k = 1
while(1):
    # gap = []
    # for i in range(n):
    #     gap.append(k - a[i])


    tmp = k
    print("k : {}".format(k))
    while tmp > 0:
        gap = []
        for i in range(n):
            gap.append(tmp - a[i])
        print("gap : {}".format(gap))
        idx = gap.index(MIN(gap))
        print("min gap : {}".format(MIN(gap)))
        print("idx : {}".format(idx))
        gap[idx] = -1
        tmp = tmp - a[idx]
        print("tmp : {}".format(tmp))

    #
    # print("gap : {}".format(gap))
    # print("k : {}".format(k))

    if tmp != 0:
        print(k)
        break

    elif tmp == 0:
        k += 1
