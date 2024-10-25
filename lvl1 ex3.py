'''lvl1 ex3'''
a=[]
b=[]
c=[]
d=[]
print('Введите значения, которые хотели бы внести в первый список:')    
for i in range(4):
    a.append(int(input()))
print('Введите значения, которые хотели бы внести во второй список:')    
for i in range(4):
    b.append(int(input()))
for i in range(4):
    c.append(a[i]+b[i])
for i in range(4):
    d.append(a[i]-b[i])
print(c,d) 