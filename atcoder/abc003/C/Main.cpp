#include <iostream>
#include <vector>
#include <algorithm>
#define max(A,B) A>B ? A : B

using namespace std;

int N,K;
vector<double> R;
double dp[100][100]; //dp[i][j]: i番目以降から

double rec(int i, int k){
    if(i<N && k>=0){
        cout<<i<<endl;
        return max((rec(i+1,k-1)+R[i])/2, rec(i+1,k));
    }else return 0;
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>K;
    for(int i = 0; i < N; i++){
        int n; cin>>n;
        R.push_back(n);
    }
    cout<<rec(0, K)<<endl;
    return 0;
}