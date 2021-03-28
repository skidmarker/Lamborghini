def solution(jobs):
    job_cnt = len(jobs)
    time = 0
    result = []
    while job_cnt > 0:
        queue = []
        temp = []
        for job in jobs:
            if job[0] <= time:
                queue.append(job)
            else:
                temp.append(job)
        queue.sort(key=lambda x: x[1])
        if queue:
            job = queue.pop(0)
        else:
            time += 1
            continue
        result.append(time - job[0] + job[1])
        time += job[1]
        job_cnt -= 1
        jobs = temp + queue
    answer = sum(result) // len(result)
    return answer