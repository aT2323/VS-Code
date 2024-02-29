s = input().split()
list = [[s[0]]]
for i in range (1, len(s)):
    if s[i] == s[i-1]:
        list[len(list)-1].append(s[i])
    else:
         list.append([s[i]])

print(list)