#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int n,a,b;
    cin>>n>>a>>b;
    int ans = a+b-n;
    cout<<min(a,b)<<" "<<(ans<0?0:ans)<<endl;
    return 0;
}
