#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string n;
    cin>>n;
    for(auto c : n)
        cout<<(c=='9'?'1':'9');
    cout<<endl;
    return 0;
}
