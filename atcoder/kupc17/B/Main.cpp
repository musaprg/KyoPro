#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cstdio>
#define ll long long int
#define INFTY (1<<21)

using namespace std;

ll N,S,T;

// ll geth(ll t){
//     for(ll i = 0; i < N; i++){
//         ll tmp = 1<<i;
//         cout<<tmp<<endl;
//         if(tmp>t) return i-1;
//         else continue;
//     }
//     return N-1;
// }
int ans = 0;
bool traverse(int x, int c){
    if(x==T){
        ans = c;
        return true;
    } else if(x>T) return false;
    else{
        return traverse(2*x, c+1) || traverse(2*x+1, c+1);
    }
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>S>>T;
    cout<<(traverse(S, 0) ? ans : -1)<<endl;
    return 0;
}