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

int main(void){
    cin.sync_with_stdio(false);
    ll N,M;
    cin>>N>>M;
    vector<ll> aa;
    REP(i,N){
        ll a;
        cin>>a;
        aa.push_back(a);
    }
    REP(i,M){
        sort(aa.begin(), aa.end());

        ll b,c;
        cin>>b>>c;
        auto t = upper_bound(ALL(aa), aa[0]);
        t--;
        while(b!=0){
            *t = 0
            if(t==aa.begin()) break;
            t--;
        }
        REP(ii,N){
            if(b==0) break;
            if(aa[ii]<c){
                aa[ii] = c;
                b--;
            }
        }
    }
    cout<<accumulate(aa.begin(), aa.end(), 0LL)<<endl;
    return 0;
}
