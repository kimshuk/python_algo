formula = input().split('-')

num = []
for i in formula:
    total = 0
    s = i.split('+')
    for x in s:
        total += int(x)
    num.append(total)
n = num[0]
for t in range(1, len(num)):
    n -= num[t]
print(n)