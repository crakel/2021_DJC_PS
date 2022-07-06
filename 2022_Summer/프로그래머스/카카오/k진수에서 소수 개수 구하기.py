def solution(id_list, report, k):
    answer = {}
    dic = {}
    for id in id_list:
        if id not in dic:
            dic[id] = []
            answer[id] = 0

    for r in report:
        a, b = r.split()

        if a not in dic[b]:
            dic[b].append(a)

    for key, value in dic.items():
        if len(value) >= k:
            for v in value:
                answer[v] += 1

    return list(answer.values())
