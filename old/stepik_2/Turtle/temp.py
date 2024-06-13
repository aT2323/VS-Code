text = open('nums.txt', 'r')
print(sum(map(int, map(lambda x : x.strip() if x.strip().isdigit() else 0, text))))
text.close()