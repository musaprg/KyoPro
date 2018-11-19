#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int a,b,n; cin>>a>>b>>n;
    for(;;){
        if(n%a==0&&n%b==0) break;
        n++;
    }
    cout<<n<<endl;
    return 0;
}
