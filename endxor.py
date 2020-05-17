from sys import stdin
t=int(stdin.readline())
while(t):
    t-=1
    n,q=map(int,stdin.readline().split())
    arr=[int(n) for n in stdin.readline().split()]
    e,o=0,0
    for i in arr:
        temp=bin(i)[2:]
        if(temp.count("1")%2==0):
            o+=1
        else:
            e+=1
    while(q):
        q-=1
        p=int(stdin.readline())
        if(bin(p)[2:].count("1")%2==0):
            print(o,e)
        else:
            print(e,o)
