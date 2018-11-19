#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int n,x;
    cin>>n>>x;
    int a=n-x,b=x-1;
    cout<<(a>b?b:a)<<endl;
    return 0;
}
