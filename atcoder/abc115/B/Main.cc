#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    vector<int> pp;
    for(int i = 0; i < N; i++){
        int tmp;
        cin>>tmp;
        pp.emplace_back(tmp);
    }
    sort(pp.begin(), pp.end());
    int sum = accumulate(pp.begin(), pp.end(), 0);
    sum -= pp[pp.size()-1]/2;
    cout<<sum<<endl;
    return 0;
}
