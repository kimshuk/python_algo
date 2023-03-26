with open('enter.txt', 'r') as file:
    my_string = file.read()

enter = my_string.split('\n')
adv_member = sorted(list(map(int, enter[1].split())))
result = 0
count = 0

for x in adv_member:
    count += 1
    print('el:',x)
    print('length:',len(adv_member))
    print('adv_member first:', adv_member[0])
    print(adv_member)
    if count >= x:
        result += 1
        count = 0

print(result)