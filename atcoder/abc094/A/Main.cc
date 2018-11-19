#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,b,x;
    cin>>a>>b>>x;
    cout<<((a>x||(a+b)<x)?"NO":"YES")<<endl;
    return 0;
}
