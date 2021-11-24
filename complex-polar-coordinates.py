import math
import cmath
def xndy(i):
    l=list(i)[1:len(i)]
    op='+'
    if '-' in l:
        op='-'
    if i[0]!='-':
        x=int(''.join(list(i)[0:list(i).index(op)]))
        y=int(''.join(list(i)[list(i).index(op)+1:list(i).index('j')]))
        
    elif i[0]=='-':
        x=int('-'+''.join(list(l)[0:list(l).index(op)]))
        y=int(''.join(list(i)[list(l).index(op)+2:list(i).index('j')]))
    return [x,y,op]
o=xndy(input())
x=o[0]
y=int(int(o[2]+'1')*o[1])
r=(str(math.sqrt((x**2)+(y**2))))
phi=(cmath.phase(complex(x,y)))
print(f'polar coordinates are: ({r},{phi})')