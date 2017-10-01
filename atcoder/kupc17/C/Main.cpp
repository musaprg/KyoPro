#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#define ll long long int

using namespace std;

ll A;
string S;
unordered_map<string, ll> dp;

ll shash(string s){
    if(dp[s]!=0) return dp[s];
    else{
        ll a = 1, str=0;
        for(int i = 0; i < s.size(); i++){
            a *= A;
            str += a * (s[i]-'a'+1);
        }
        return dp[s] = str;
    }
}

// string ans;

// bool rec(ll a, ll k, string str){
//     cout<<"Now str = "<<str<<endl;
//     bool res;
//     if(k==0){
//         ans = str;
//         return true;
//     }
//     if(k<0) return false;
//     for(int i = 26; i >= 1; i--){
//         string tmp(1, char('a'+i-1));
//         res = rec(a*A,k-(a*i),str+tmp);
//         if(res) break;
//     }
//     return res;
// }

bool rec(ll a, ll k, string str){
    cout<<"Now str = "<<str<<endl;
    bool res;
    if(k==0){
        ans = str;
        return true;
    }
    if(k<0) return false;
    for(int i = 26; i >= 12; i--){
        string tmp(1, char('a'+i-1));
        if(dp[str+tmp]==0){
            dp[str+tmp] = a*i;
        }
        // res = rec(a*A,k-(a*i),str+tmp);
        if(res) break;
    }
    return res;
}


int main(void){
    cin.sync_with_stdio(false);
    cin>>A>>S;
    // cout<<shash(S)<<endl;
    // int cursor = 0;
    // while(cursor<S.size()){
        
    // }
    // string s;
    // rec(1,shash(S),s);
    cout<<ans<<endl;
    return 0;
}