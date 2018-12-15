#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

ll solve(string &a){
    ll count = 0;
    ll n = a.size();
    if(n>1){
        string b(a.begin(), a.begin()+n/2);
        string c(a.begin() + n/2, a.end());
        count += solve(b);
        count += solve(c);
        for(ll i=0,j=0,k=0; i<n; i++){
            if(k==c.size())         a[i] = b[j++];
            else if(j==b.size())    a[i] = c[k++];
            else if(b[j] >= c[k])   a[i] = b[j++];
            else{
                a[i] = c[k++];
                count += n/2 - j;
            }
        }
    }
    return count;
}

int main(void){
    cin.sync_with_stdio(false);
    string s;
    cin>>s;
    cout<<solve(s)<<endl;

    return 0;
}
