num = 1 

while num  < 10:
    print(num)
    num += 1

while num  < 20:
    print(num)
    if num  == 10:
        break
    num += 1

while num  < 21:
    num += 1
    if num  == 12:
        continue
    print(num)
    