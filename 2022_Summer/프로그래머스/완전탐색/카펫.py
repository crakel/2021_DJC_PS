import itertools


def solution(brown, yellow):
    answer = []
    r = 0
    c = 0
    able = []

    def get_divisor(num):
        res = []
        for i in range(1, num + 1):
            if num % i == 0:
                res.append(i)
        return res

    divisor = get_divisor(brown + yellow)
    able = list(itertools.product(divisor, repeat=2))
    lst = []

    for a in able:
        if a[0] * a[1] == brown + yellow:
            lst.append(a)

    for l in lst:
        x, y = l[0], l[1]
        if x * 2 + y * 2 - 4 == brown:
            return [y, x]