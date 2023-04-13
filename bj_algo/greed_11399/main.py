# N을 입력받기
enter = int(input())
people = list(map(int, input().split()))
people.sort()
total = 0

for i in range(len(people)):
    total += sum(people[0:i+1])
print(total)

