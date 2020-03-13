import re
j=1;y=[]
op=['+','-','*','/']
x=input("enter expresion: ")
m=re.split("([+-/*])",x)
def comp(m,j):
    for word in m:
        if word in op:
            y.append(''.join(m[0:3]))
            m.pop(0);m.pop(0)
            m[0]='t'+str(j)
            j+=1

    return m,j
while len(m)>1:
    m,j=comp(m,j)
k=len(y)
y.reverse()
for i in range(0,len(y)):
    print('t'+str(k)+'='+y[i])
    k-=1