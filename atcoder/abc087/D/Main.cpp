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

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,M; cin>>N>>M;
    int D[N+1][N+1];
    for(int i = 0; i <= N; i++)
        for(int j = 0; j < N+1; j++)
            D[i][j] = -1;
    for(int i = 0; i < M; i++){
        int l,r,d; cin>>l>>r>>d;
        D[l][r] = D[r][l] = d;
    }
    for(int i = 1; i <= N; i++){
        for(int j = 2; j <= N; j++){
            for(int k = 3; k <= N; k++){
                if(D[i][j]==-1 || D[j][k]==-1 || D[i][k]==-1) continue;
                // cout<<i<<" "<<j<<" "<<k<<endl;
                if(D[i][k] != D[i][j] + D[j][k]){
                    cout<<"No"<<endl;
                    return 0;
                }
            }
        }
    }

    cout<<"Yes"<<endl;

    return 0;
}