#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int s;
    cin>>s;
    vector<int> aa;
    aa.emplace_back(s);
    while(true){
        int ba = aa[aa.size()-1];
        int a = ba%2==0?ba/2:3*ba+1;
        auto result = find(aa.begin(), aa.end(), a);
        if(result == aa.end())
            aa.emplace_back(a);
        else{
            cout<<aa.size()+1<<endl;
            break;
        }
    }
    return 0;
}
