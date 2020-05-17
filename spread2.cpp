#include <iostream>
using namespace std;

int main() {
	int T;
	long long N;
	long long arr[100000],pre_arr[100000];
	cin>>T;
	long long p_know,day,temp;
	while(T--)
	{
	    p_know=1;
	    cin>>N;
	    for(long long i=0;i<N;i++)
	    {
	        cin>>arr[i];
	    }
	    
	    pre_arr[0]=arr[0];
	    for(long long i=1;i<N;i++)
	        pre_arr[i]=pre_arr[i-1]+arr[i];
        day=0;;
	    while(p_know<N)
	    {
	        day++;
	        p_know+=pre_arr[p_know-1];
	    }
	    std::cout << day << std::endl;
	}
	return 0;
}

