########### RSA Algorithm #############
#######################################

## Prime number generation
n=1000
res=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        res.append(str(i))

## Key generation
p=int(input("Выберите простое число p из списка "+' '.join(res)+': '))
a=0
res1=[]
while a<len(res):
    res1.append(int(res[a]))
    a=a+1

while (p in res1)==False:
                p=int(input('Вы ввели не простое число, повторите попытку: '))
q=int(input("Выберите простое число q из списка: "))

while (q in res1)==False:
    q=int(input('Вы ввели не простое число, повторите попытку: '))

n=p*q
fn=(p-1)*(q-1)

lst=[] #простые числа
for i in range(2,fn):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst.append(i)

e=[] #взаимно простые числа

## Euclidean Algorithm for Determining the Least Common Divisor
for i in lst:
    i1=i
    n1=n
    while n1>i1 and (n1-i1)>=0:
        n1-=i1
        while n1<i1 and (i1-n1)>=0:
            i1-=n1
    if i1==1 and n1==1:
        e.append(i)
    else:
        continue
d=[]
for i in e:
    for k in range(100000):
        if (fn*k+1)%i==0:
            d.append(int((fn*k+1)/i))
            break
    if (fn*k+1)%i!=0:
        d.append(0)

print('Существует ',len(e),' пар ключей.')
que=int(input('Сколько пар ключей вам вывести? '))
count=0
for i in range(len(d)):
    if d[i]==0:
        continue
    else:
        print('Открытый ключ: ',n,',',e[i])
        print('Закрытый ключ: ',d[i])
        count+=1
    if count>=que:
        break