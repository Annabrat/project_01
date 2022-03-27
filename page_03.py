s = '8 (912) 645-23-56'
new_s = ''

for i in s:
    if i.isdigit() is True:
        new_s += i
    else:
        pass

print(new_s)
