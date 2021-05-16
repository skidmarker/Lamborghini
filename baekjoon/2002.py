N = int(input())
answer = 0
cars = []
front_dict = dict()
for i in range(N):
    car = input()
    front_dict[car] = cars[:]
    cars.append(car)
    

exit_cars = []
for i in range(N):
    car = input()
    exit_cars.append(car)

for i in range(N):
    car = exit_cars[i]
    back_arr = exit_cars[:i:-1]
    for bc in back_arr:
        if bc in front_dict[car]:
            answer += 1
            break

print(answer)