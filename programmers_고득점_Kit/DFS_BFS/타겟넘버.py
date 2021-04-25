cnt = 0

def solution(numbers, target):
    global cnt

    answer = 0

    def dfs(n, w, k, target, numbers):
        global cnt
        if n == k:
            if w == target:
                cnt += 1
                return
        else:
            dfs(n + 1, w - numbers[n], k, target, numbers)
            dfs(n + 1, w + numbers[n], k, target, numbers)
    dfs(0, 0, len(numbers), target, numbers)
    answer = cnt

    return answer