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

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    vector<int> a;
    for(int i = 0; i < N; i++){
        int t; cin>>t; a.push_back(t);
    }
    sort(a.begin(), a.end(), greater<int>());
    int ans=0;
    for(int i = 0; i < N; i++){
        if(i%2==0) ans+=a[i];
        else ans-=a[i];
    }
    cout<<ans<<endl;
    return 0;
}