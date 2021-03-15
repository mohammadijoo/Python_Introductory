items = []
num = [x for x in input("Enter some binary numbers, separated by comma: ").split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)

print(','.join(items))
