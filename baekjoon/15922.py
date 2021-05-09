N = int(input())
x, y = map(int, input().split())
result = 0

for _ in range(N - 1):
    temp_x, temp_y = map(int, input().split())

    if x <= temp_y <= y:
        continue
    elif x <= temp_x <= y and not x <= temp_y <= y:
        y = temp_y
    else:
        result += y - x
        x, y = temp_x, temp_y

print(result + (y - x))