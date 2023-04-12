# N을 입력받기
pos = str(input())
plate = 8

x, y = ord(pos[0]) - 96, int(pos[1])
print(x, y)

count = 0
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-2, 1), (-1, 2)]

for s in steps:
    nx = x + s[0]
    ny = y + s[1]
    print('x', nx, 'y', ny)
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1
    print('=======')

print('count', count)
