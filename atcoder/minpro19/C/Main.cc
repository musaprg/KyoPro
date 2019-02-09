#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll K,A,B;
    cin>>K>>A>>B;
    ll ans;
    ll tmp = K-(A-1);
    if(B-A<=2 || tmp<0) ans = K+1;
    else ans = A + tmp/2*(B-A) + tmp%2; 
    cout << ans << endl;
    return 0;
}
