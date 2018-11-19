#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string s;
    cin>>s;
    sort(s.begin(), s.end());
    cout<<((s == "abc")?"Yes":"No")<<endl;
    return 0;
}
