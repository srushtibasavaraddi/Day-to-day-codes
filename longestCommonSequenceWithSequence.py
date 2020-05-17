s1=input()
s2=input()
def LCS(s1,s2):
    l1,l2=len(s1),len(s2)
    arr=[[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if(s1[i-1]==s2[j-1]):
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i][j-1],arr[i-1][j])
    
    #print(ar)
    s=""
    '''
    for j in arr:
        print(j)
    '''
    i = l1 
    j = l2 
    
    while i > 0 and j > 0: 
  
        if s1[i-1] == s2[j-1]: 
            s = s+s1[i-1] 
            i-=1
            j-=1
         
        elif arr[i-1][j] > arr[i][j-1]: 
            i-=1
        else: 
            j-=1   
    s=s[::-1]
    
    print(s,end="")
    #print(arr)
    #return arr[l1][l2]

LCS(s1,s2)
    
