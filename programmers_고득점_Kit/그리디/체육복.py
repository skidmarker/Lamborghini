def solution(n, lost, reserve):
    lost_stu = set(lost)
    reserve_stu = set(reserve)
    answer = n - len(lost_stu | reserve_stu)
    only_one = reserve_stu & lost_stu
    
    
    for num in lost:
        if num not in reserve_stu:
            left = num - 1
            right = num + 1
            if left in reserve and left not in only_one:
                answer += 1
                only_one.add(left)
            elif right in reserve and right not in only_one:
                answer += 1
                only_one.add(right)
    answer += len(reserve)
    return answer