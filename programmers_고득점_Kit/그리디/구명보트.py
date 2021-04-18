def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left = 0
    right = len(people) - 1
    now_weight = 0
    while left <= right:
        now_weight += people[left]
        left += 1
        if now_weight + people[right] <= limit:
            right -= 1
        answer += 1
        now_weight = 0
    return answer