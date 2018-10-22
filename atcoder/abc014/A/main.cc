#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,b;
    cin>>a>>b;
    cout<<(a%b==0?0:b-(a%b))<<endl;
    return 0;
}
