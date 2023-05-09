import math

N, M = list(map(int, input().split(' ')))

package = []
single = []
result = []
for _ in range(M):
    p, s = list(map(int, input().split(' ')))
    package.append(p)
    single.append(s)

package.sort()
single.sort()

result.append(package[0]*(math.ceil(N/6)))
result.append(package[0]*(N//6)+single[0]*(N%6))
result.append(single[0]*N)
print(min(result))