import math

# N을 입력받기
weight = int(input())
bagCount = 0

while weight >= 0:
    if weight % 5 == 0:
        bagCount += (weight // 5)
        print(bagCount)
        break
    weight -= 3
    bagCount += 1
else:
    print(-1)