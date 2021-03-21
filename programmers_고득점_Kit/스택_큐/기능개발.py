# def solution(progresses, speeds):
#     answer = []
#     queue = []
#     for i in range(len(speeds)):
#         queue.append([progresses[i], speeds[i]])
#     queue.append(-1)
#     finished_work = 0
#     while queue:
#         todo = queue.pop(0)
#         if todo == -1:
#             while True:
#                 if queue[0][0] >= 100:
#                     queue.pop(0)
#                     finished_work += 1
#                     if len(queue) == 0:
#                         break
#                 else:
#                     break
#             if finished_work:
#                 answer.append(finished_work)
#                 finished_work = 0
#             if len(queue) == 0:
#                 break
#             queue.append(-1)
#         else:
#             todo[0] += todo[1]
#             queue.append(todo)
#     return answer

def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(speeds)):
        queue.append([progresses[i], speeds[i]])
    
    while queue:
        todo = queue[0]
        required_days = round((100 - todo[0]) / todo[1])
        if (100 - todo[0]) / todo[1] > required_days:
            required_days += 1
        finished_work = 0
        for i in range(len(queue)):
            queue[i][0] += queue[i][1] * required_days
        
        while True:
            if queue[0][0] >= 100:
                finished_work += 1
                queue.pop(0)
                if len(queue) == 0:
                    break
            else:
                break
        answer.append(finished_work)
        finished_work = 0
    
    return answer