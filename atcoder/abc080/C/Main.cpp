#include <iostream>
#include <vector> //可変長配列
#include <queue> //キュー
#include <unordered_map> //ハッシュ連想配列
#include <numeric>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define ll long long int
#define INFTY (1<<21)
#define maxN 100

using namespace std;

int N;
int F[maxN+1][5+1][2+1];
int P[maxN+1][10+1];

int c[5+1][2+1];
int p[5+1][2+1];
int dp[5+1][2+1];

int g_cn(int j, int k){
    if(c[j][k]!=-1) return c[j][k];
    else{
        int count = 0;
        for(int i = 1; i < N+1; i++){
            count += F[i][j][k];
        }
        return c[j][k] = count;
    }
}

int g_p(int j, int k){
    if(p[j][k]!=-1) return p[j][k];
    else{
        int count = 0;
        for(int i = 1; i < N+1; i++){
            count += P[i][c[j][k]];
        }
        return p[j][k] = count;
    }
}

int rec(int j, int k){
    printf("(%d,%d)\n", j,k);
    if(dp[j][k]!=-1) return dp[j][k];
    else if(j==5){
        if(k==1) return dp[j][k] = max(
            g_p(j,k)+rec(j, 2),
            rec(j, 2)
        );
        else return dp[j][k] = max(g_p(j,k),0);
    }else{
        if(k==1) return dp[j][k] = max(
            g_p(j,k)+rec(j,2),
            rec(j,2)
        );
        else return dp[j][k] = max(
            g_p(j,k)+rec(j+1,1),
            rec(j+1,1)
        );
    }
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N;
    for(int i = 1; i < N+1; i++){
        for(int j = 1; j < 5+1; j++){
            for(int k = 1; k < 2+1; k++){
                cin>>F[i][j][k];
            }
        }
    }
    for(int i = 1; i < N+1; i++){
        for(int j = 0; j <= 10; j++){
            cin>>P[i][j];
        }
    }
    for(int i = 1; i < (5+1); i++){
        for(int j = 1; j < (2+1); j++){
            dp[i][j] = -1;
            c[i][j] = -1;
            p[i][j] = -1;
        }
    }
    cout<<rec(1,1)<<endl;

    return 0;
}