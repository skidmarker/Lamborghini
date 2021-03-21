def solution(bridge_length, weight, truck_weights):
    queue = []
    truck = truck_weights.pop(0)
    queue.append([truck, 1])
    queue.append(-1)
    time = 1
    now_acc_weight = 0
    while queue:
        target = queue.pop(0)
        if target == -1:
            time += 1
            if truck_weights:
                if now_acc_weight + truck_weights[0] <= weight:
                    new_truck = truck_weights.pop(0)
                    queue.append([new_truck, 1])
            now_acc_weight = 0
            if queue:
                queue.append(-1)
        else:
            target[1] += 1
            if target[1] <= bridge_length:
                now_acc_weight += target[0]
                queue.append(target)

    return time