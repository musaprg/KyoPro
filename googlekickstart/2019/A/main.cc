#include <bits/stdc++.h>

using namespace std;

// typedef
typedef long long ll;

// container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

// repetition
#define FOR(i,a,n) for(ll i = ((ll) a); i < ((ll) n); ++i)
#define REP(i,n) FOR(i,0,n)

//constant
const double    EPS     = 1e-10;
const double    PI      = acos(-1.0);
const int       INFTY   = (1<<21);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

void printv(vector<int>& v){
    for(auto&& val : v){
        cerr<<val<<" ";
    }
    cerr<<endl;
}

int main(void){
    cin.sync_with_stdio(false);
    int T; cin>>T;
    for(int ii = 0; ii < T; ii++){
        ll N,P;
        cin>>N>>P;
        debug(N);
        debug(P);
        vector<int> S,ds;
        for(int i = 0; i < N; i++){
            int s; cin>>s;
            S.push_back(s);
        }
        sort(S.begin(), S.end());
        printv(S);
        
        // 1dim imos
        ds.push_back(0);
        for(int i = 0; i < N-1; i++){
            ds.push_back(ds[i]+S[i+1]-S[i]); 
        }
        printv(ds);

        ll ans = INFTY;
        int lidx;
        for(int i = 0; i <= N-P; i++){
            int t = i+P-1;
            ll tmp = ds[t]-ds[i];
            if(tmp<ans){
                lidx = i;
                ans = tmp;
            }
        }
        int ridx = lidx+P-1;
        ll res = 0;
        for(int i = lidx; i <= ridx; i++){
            res += S[ridx]-S[i];
        }
        cout<<"Case #"<<ii+1<<": "<<res<<endl;
    }
    return 0;
}
