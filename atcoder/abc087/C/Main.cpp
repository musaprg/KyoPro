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

int N,A[2][100];

int rec(int i, int j){
    if(j==N) return 0;
    else if(i==1)
        return A[i][j] + rec(i,j+1);
    else
        return A[i][j] + max(rec(i,j+1),rec(i+1,j));
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N;
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < N; j++){
            cin>>A[i][j];
        }
    }
    cout<<rec(0,0)<<endl;
    return 0;
}