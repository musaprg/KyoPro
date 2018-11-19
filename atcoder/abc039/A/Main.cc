#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,b,c; cin>>a>>b>>c;
    cout<<(b*c*2+a*(b+c)*2)<<endl;
    return 0;
}
