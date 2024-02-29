def chunked(s, n):
    list = []
    while s != []:
        list.append([])
        for _ in range(n):
            if s == []:
                break
            else:
                list[-1].append(s.pop(0))
    return list
s = input().split()
n = int(input())
print(chunked(s,n))
