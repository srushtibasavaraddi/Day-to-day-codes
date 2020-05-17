#technique used to find pairs in linear time, know as 2 point technique
# here used to find difference equal to d can be used for sum as well
def findPairs():
    c,i,j=0,0,0
    while(j<n):
        diff=arr[j]-arr[i]
        if(diff==d):
            c+=1
            j+=1
            i+=1
        elif(diff>d):
            i+=1
        else:
            j+=1
        
        # print(c,i,j)
    return c
n,d=map(int,input().split())
arr=sorted([int(n) for n in input().split()])
print(findPairs())
# Enter your code here. Read input from STDIN. Print output to STDOUT
