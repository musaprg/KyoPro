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
    int N,D;
    cin>>N>>D;
    int* X = new int[N];
    for(int i = 0; i < N; i++){
        cin>>X[i];
    }
    int ans = 0;
    for(int i = 0; i < N-2; i++){
        for(int j = i+1; j < N-1; j++){
            for(int k = j+1; k < N; k++){
                if((X[j]-X[i])<=D && (X[k]-X[j])<=D && (X[k]-X[i])>D){
                    ans++;
                }
            }
        }
    }
    cout<<ans<<endl;

    return 0;
}