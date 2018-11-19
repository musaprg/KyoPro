#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,b,c,ans=0;
    cin>>a>>b>>c;
    if(a>b)
        cout<<(c/b+(c%b)/a)<<endl;
    else
        cout<<(c/a+(c%a)/b)<<endl;
    return 0;
}
