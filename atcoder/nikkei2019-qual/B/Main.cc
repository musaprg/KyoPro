#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int n;
    string a,b,c;
    cin>>n>>a>>b>>c;
    int ans = 0;
    for(int i = 0; i < n; i++){
        if(a[i]==b[i]){
            if(a[i]!=c[i]) ans++;
        }
        else if(b[i]==c[i]){
            if(a[i]!=c[i]) ans++;
        }
        else if(a[i]==c[i]){
            if(b[i]!=c[i]) ans++;
        }
        else{ //3つとも違う
            ans += 2;
        }
    }
    cout<<ans<<endl;
    return 0;
}
