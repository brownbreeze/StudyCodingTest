#include <iostream>
using namespace std;
int main() {
    int cnt,i,j,max=0;
    int data[1001]={0};
    int rst[1001]={0};

    cin>>cnt;
    for(i = 1 ; i<=cnt;i++)
        cin>>data[i];
    
    for(i=1;i<=cnt;i++)
    {
        int min = 0;
        for(j=0;j<i;j++)
        {
            if(data[i]>data[j])
                if(min<rst[j]) min = rst[j];
        }
        rst[i] = min+1;
        if(max<rst[i]) max= rst[i];
    }
    cout<<max<<endl;
    return 0;
}
