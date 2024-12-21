start = int(input())
end = int(input())

notSymmetrical = ["2", "3", "4", "5", "7"]

count = 0

for i in range(start, end + 1):
    str(i)
    length = len(i)
    for e in notSymmetrical:
        if e not in i:
            continue
        else:
            if len(i) % 2 == 1:
                if i[len]


print(count)
