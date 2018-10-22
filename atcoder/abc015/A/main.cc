#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string a,b;
    cin>>a>>b;
    cout<<(a.size()>b.size()?a:b)<<endl;
    return 0;
}
