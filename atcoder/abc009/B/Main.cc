#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    vector<int> aa;
    int N;
    cin>>N;
    for(int i = 0; i < N; i++){
        int a;
        cin>>a;
        aa.push_back(a);
    }
    sort(aa.begin(),aa.end());
    cout<<aa[aa.size()-2]<<endl;
    return 0;
}
