def solution(s):
    answer = 1e9

    for i in range(1, len(s)):
        cur = s[:i]
        cnt = 1
        res = ""

        for j in range(i, len(s) + i, i):

            if cur == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += cur
                else:
                    res += str(cnt) + cur
                cur = s[j:j + i]
                cnt = 1

        answer = min(answer, len(res))

    return answer