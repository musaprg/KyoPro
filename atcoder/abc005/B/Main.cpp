#include <iostream>
#include <vector>
#include <algorithm>
#define INF (2<<29)
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    ll n, min=INF;
    while(cin>>n)
        if(n<min) min = n;
    cout<<min<<endl;
    return 0;
}