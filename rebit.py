def gcd(a,b):
    if(a==0):
        return (b,0,1)
    else:
        g,y,x=gcd(b%a,a)
        return (g,x-(b//a)*y,y)

def modd(a, m):
    g,x,y=gcd(a,m)
    return (x%m)

orr=[[(0,0)],[(0,1),(1,0),(1,2),(2,1),(1,3),(3,1),(3,2),(2,3),(1,1)],[(0,2),(2,0),(2,2)],[(0,3),(3,0),(3,3)]]
andd=[[(0,0),(0,1),(1,0),(0,3),(3,0),(2,0),(0,2),(2,3),(3,2)],[(1,1)],[(2,1),(1,2),(2,2)],[(3,1),(1,3),(3,3)]]
xorr=[[(0,0),(1,1),(2,2),(3,3)],[(1,0),(3,2),(2,3),(0,1)],[(0,2),(2,0),(1,3),(3,1)],[(0,3),(3,0),(1,2),(2,1)]]
def solve(a,b,o):
    r=[]
    if(o=='|'):
        arr=orr
    elif(o=="&"):
        arr=andd
    else:
        arr=xorr
    for j in range(4):    
        temp=0
        for i in arr[j]:
            temp+=a[i[0]]*b[i[1]]
        r.append(temp)
    return r

t=int(input())
while(t):
    t-=1
    s=input()
    ls=list(s)
    stack=[]
    for i in s:
        if(i==")"):
            arr=[]
            temp=stack.pop()
            arr.append(temp)
            while(temp!="("):
                temp=stack.pop()
                arr.append(temp)
            r=solve(arr[0],arr[2],arr[1])
            stack.append(r)
        elif(i=="#"):
            stack.append([1]*4)
        else:
            stack.append(i)
    # print(stack)
    m=modd(sum(stack[0]),998244353)
    print((stack[0][0]*m)%998244353,end=" ")
    print((stack[0][1]*m)%998244353,end=" ")
    print((stack[0][2]*m)%998244353,end=" ")
    print((stack[0][3]*m)%998244353,end=" ")
    print()