#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,d; cin>>a>>d;
    int b = (a+1)*d, c = a*(d+1);
    cout<<(b>c?b:c)<<endl;
    return 0;
}
