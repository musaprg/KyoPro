#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    double s,e,ans=0;
    for(int i = 0; i < 3; ++i){
        cin>>s>>e;
        ans+=s*(e/10);
    }
    cout<<int(ans)<<endl;
    return 0;
}
