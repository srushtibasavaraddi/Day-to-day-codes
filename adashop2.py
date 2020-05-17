arr=[[8,8],[7,7],[8,6],[7,5],[8,4],[7,3],[8,2],[7,1],[6,2],[5,1],[4,2],[3,1],[8,6],
[6,8],[1,3],[2,4],[1,5],[2,6],[1,7],[2,8],[3,7],[4,8]]
t=int(input())
while(t):
    t-=1
    r,c=map(int,input().split())
    if(r==1 and c==1):
        print(len(arr))
        for i in arr:
            print(i[0],i[1])
    else:
        if(r==c):
            print(len(arr)+1)
            print(1,1)
            for i in arr:
                print(i[0],i[1])
        else:
            print(len(arr)+2)
            l=r+c
            l=l//2
            print(l,l)
            print(1,1)
            for i in arr:
                print(i[0],i[1])
            