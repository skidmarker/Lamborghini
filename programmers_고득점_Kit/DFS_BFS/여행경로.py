def solution(tickets):
    tickets = list(map(tuple, tickets))
    tickets.sort(key=lambda x: x[1])

    def dfs(now, p, t_arr):
        if len(t_arr) == 0:
            return p

        for i in range(len(t_arr)):
            t = t_arr[i]
            if now == t[0]:
                n_t_arr = t_arr[:i] + t_arr[i+1:]
                d = t[1]
                res = dfs(d, p+[d], n_t_arr)
                if res:
                    return res
        return False

    answer = dfs("ICN", ["ICN"], tickets)

    return answer