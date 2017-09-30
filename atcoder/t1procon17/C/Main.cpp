#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll N; cin>>N;
    ll h,n;
    for(h = 1; h <= 3500; h++){
        for(n = 1; n <= 3500; n++){
            ll a = N*h*n, b = 4*h*n-N*(h+n);
            if(b<=0) continue;
            if(a>b && a%b==0){
                cout<<h<<" "<<n<<" "<<a/b<<endl;
                return 0;
            }
        }
    }
    return 0;
}