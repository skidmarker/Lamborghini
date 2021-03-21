def solution(priorities, location):
    sorted_priorities = sorted(priorities, reverse=True)
    queue = []
    for i in range(len(priorities)):
        temp = [priorities[i], False] # 우선순위, 요청 여부
        if i == location:
            temp[1] = True
        queue.append(temp)
    order = 1
    while queue:
        now_paper = queue.pop(0)
        if now_paper[0] < sorted_priorities[0]:
            queue.append(now_paper)
        else:
            if now_paper[1] == True:
                return order
            else:
                order += 1
                sorted_priorities.pop(0)
            
    return order