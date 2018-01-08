data = 'bAse730onE4'
x = 0
y = 0
z = 0
for i in data:
    if 58>ord(i)>47:
        x += 1
    if 91>ord(i)>64: 
        y += 1
    if 123>ord(i)>96:
        z += 1
if x > 0 and y > 0 and z > 0:
    a = True
else:
    a = False

print(a)
