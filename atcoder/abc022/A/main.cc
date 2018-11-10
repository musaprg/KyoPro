#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,S,T,W; cin>>N>>S>>T>>W;
    int ans = (S<=W&&W<=T)?1:0;
    for(int i=0;i<N-1;i++){
        int A; cin>>A;
        W += A;
        ans += (S<=W&&W<=T)?1:0;
    }
    cout<<ans<<endl;

    return 0;
}
