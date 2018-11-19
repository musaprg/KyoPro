#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string N;
    cin>>N;
    cout<<((N[0]==N[1]&&N[1]==N[2]&&N[2]==N[3])?"SAME":"DIFFERENT")<<endl;
    return 0;
}
