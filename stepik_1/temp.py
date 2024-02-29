s = input()
seq = s.split("О")  # убираем всех орлов и группируем решек
print (seq)
mx = 0  # максимум подряд идущих решек
for el in seq:
    mx = max(mx, el.count("Р"))
    
print(mx)