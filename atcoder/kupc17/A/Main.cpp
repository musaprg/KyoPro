#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cstdio>
#define ll long long int
#define INFTY (1<<21)
#define NMAX 50
#define KMAX 1000

using namespace std;

int N,K;
vector<int> as;
int dp[NMAX+1][KMAX+1]; //memo

int rec(int i, int k, int ans){
    if (dp[i][k] != -1){
        return dp[i][k];
    }
    int res;
    if(i==N){
        return k<=0 ? ans : INFTY;
    }else if(k<=0){
        return ans;
    }else{
        res = min(
            rec(i+1, k, ans),
            rec(i+1, k-as[i], ans+1)
        );
    }
    return dp[i][k] = res;
}

// int rec(int i, int k, int ans){
//     int res;
//     if(i==N){
//         return k<=0 ? ans : INFTY;
//     }else if(k<=0){
//         return ans;
//     }else{
//         res = min(
//             rec(i+1, k, ans),
//             rec(i+1, k-as[i], ans+1)
//         );
//     }
//     return res;
// }

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>K;
    for(int i = 0; i < NMAX+1; i++){
        for(int j = 0; j < KMAX+1; j++){
            dp[i][j] = -1;
        }
    }
    for(int i = 0; i < N; i++){
        int a; cin>>a;
        as.push_back(a);
    }
    if(accumulate(as.begin(), as.end(), 0)<K){
        cout<<-1<<endl; return 0;
    }
    sort(as.begin(), as.end(), greater<int>());
    cout<<rec(0,K,0)<<endl;
    return 0;
}