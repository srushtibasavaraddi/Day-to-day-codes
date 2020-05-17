#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

long long n,k,q,start_text,end_text;
int text[1000000],temp,r;
char query[1000000];

void consec() 
{ 
    long long count = 0;  
    long long result = 0;
  
    for (int i = start_text; i <=end_text; i++) 
    { 
        if (text[i] == 0)
	{	 
            count = 0; 
  	}

        else
        { 
            count++;
		if(count>result)
		{
			result=count;
		}
		
		if(result==k)
		{
			break;
		} 
        } 
    } 
  
    printf("%lld\n",result); 
} 
  


int main()
{
	long long i,j=0,q_no;	
	scanf("%lld%lld%lld",&n,&q,&k);
	for(i=1000000-n;i<=999999;i++)
	{
		scanf("%d",&text[i]);
	}
	start_text=1000000-n;
	end_text=999999;	
	scanf("%s",query);
	q_no=0;
	while(q--)
	{
		
		if(query[q_no]=='!')
		{
			temp=text[end_text];
			end_text--;
			start_text--;
			text[start_text]=temp;		
		}
		
		else
		{
			consec();
		}

		q_no++;
	}
}
