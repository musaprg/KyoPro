#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

#define NMAX 100000

using namespace std;

ll n,m;
vector< ll > v;
ll key[2*NMAX][2];
ll prior[NMAX];
bool flg[NMAX];

// void setPrior(vector<int> vt){
//     sort(vt.begin(), vt.end(), greater<int>());
//     for(int i = 0; i < vt.size(); i++){
//         auto it = find(v.begin(), v.end(), vt[i]);
//         if(it != v.end()){
//             int index = distance(v.begin(), it);
//             prior[index] = v.size()-i;
//         }
//     }
// }

// ll rec(ll i, ll remkey){
//     if(i==n) return 0;
//     if(remkey==0) return 0;
//     return max(
//         rec(i+1, remkey-1),
//         rec(i+1, remkey)
//     );
// }

int main(void){
    cin.sync_with_stdio(false);
    cin>>n>>m;
    ll ans = 0;
    for(ll i = 0; i < n; i++){
        ll a; cin>>a;
        v.push_back(a);
    }
    for(ll i = 0; i < NMAX; i++){
        flg[i] = true;
    }
    // for(int i = 0; i < m; i++){
    //     int x,y; cin>>x>>y;
    //     key[i][0] = x-1;
    //     key[i][1] = y-1;
    // }
    for(ll i = 0; i < m; i++){
        ll x,y; cin>>x>>y;
        if(v[x-1]>v[y-1]){
            if(flg[x-1]){
                ans += v[x-1];
                flg[x-1] = false;
            }else if(flg[y-1]){
                ans += v[y-1];
                flg[y-1] = false;
            }
        }else{
            if(flg[y-1]){
                ans += v[y-1];
                flg[y-1] = false;
            }else if(flg[x-1]){
                ans += v[x-1];
                flg[x-1] = false;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}