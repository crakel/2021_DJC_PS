def solution(prices):
    answer = []
    for i, price in enumerate(prices):
        cur = price

        time = 0
        for j in range(i+1, len(prices)):
            #print("cur: ", price)
            #print("price[j]: ", prices[j])
            time += 1
            if prices[j] < cur:
                break
        answer.append(time)
    return answer

# stack 풀이
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # stack이 비었으면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
