#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    vector<int> n;
    for(int i=0;i<3;i++){
        int num;
        cin>>num;
        n.push_back(num);
    }
    sort(n.begin(),n.end());
    cout<<n[1]<<endl;
    return 0;
}
