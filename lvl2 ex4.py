'''lvl2 ex4'''
from array import *
from operator import index
a=[]
n=int(input('Введите количество значений в вашем списке:'))
print('Введите значения, которые хотели бы внести в список:')
for i in range(n):
    a.append(int(input()))
av=sum(a)/len(a)
for i in range(a.index(max(a))+1, len(a)):
    a[i]=av
print(a)