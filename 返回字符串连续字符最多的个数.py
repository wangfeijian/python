str = "abcdefjjsalfafesdjfe"
list = []
str_x = str[0:1]
x_num = 0
for i in range(1, len(str)):
    if str[i] in str_x:
        str_x = str_x + str[i]
    else:
        list.append(str_x)
        str_x = str[i]
    x_num += 1
if x_num == 1:
    list.append(str_x)

num = 0
for i in list:
    if len(i) > num:
        num = len(i)
print(list)
print(num)

