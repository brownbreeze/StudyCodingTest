#include <iostream>
#include <vector>

using namespace std;
int N;
vector<int> num;
int arr[10] = {0};


int main()
{
    cin>>N;
    num.resize(N);
    arr[0] = 1; arr[1] = 2; arr[2] =4;
    for(int i = 0 ; i<N; i++)
        cin>>num[i];
    
    for(int i = 3; i<10; i++)
        arr[i] = arr[i-2]+arr[i-1]+arr[i-3];
    
    for(int i = 0 ; i<N; i++)
        cout<<arr[num[i]-1]<<endl;
    return 0;
}

