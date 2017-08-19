#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N,K;
vector<double> R;

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>K;
    for(int i = 0; i < N; i++){
        int n; cin>>n;
        R.push_back(n);
    }
    sort(R.begin(), R.end());
    // vector<double>::iterator ir = R.begin();
    double ans = 0;
    for(int i = R.size()-K; i < R.size(); i++){
        ans += R[i]; ans /= 2;
    }
    printf("%.6f\n", ans);
    return 0;
}