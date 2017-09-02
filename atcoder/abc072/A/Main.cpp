#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll X,t; cin>>X>>t;
    cout<<(X<t?0:X-t)<<endl;
    return 0;
}