#include <bits/stdc++.h>

#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N;
    cin>>N;
    map<string,int> m;
    for(int i = 0; i < N; ++i){
        string s;
        cin>>s;
        if(m.find(s)!=m.end()){
            m[s] += 1;
        }else{
            m[s] = 1;
        }
    }
    pair<string,int> ans;
    for(auto itr = m.begin(); itr != m.end(); ++itr){
        if(ans.second < itr->second){
            ans = make_pair(itr->first, itr->second);
        }
    }
    cout<<ans.first<<endl;
        
    return 0;
}
