s = input()

count = 0
memory = 0
for i in range(len(s)):
    if s[i] == 'Р':
        count += 1
    else:
        if count > memory:
            memory = count
        count = 0
if count > memory:
     memory = count
    
print(memory)