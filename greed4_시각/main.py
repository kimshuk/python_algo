# N을 입력받기
n = int(input())
print(n)

check = '3'
sec = 60
min = 60
count = 0

for z in range(n + 1):
    for y in range(min):
        for x in range(sec):
            if check in str(x) or check in str(y) or check in str(z):
                count += 1

print('count:', count)
