#include <bits/stdc++.h>

using namespace std;

// typedef
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long> vll;
typedef vector<string> vs;

// container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

// repetition
#define FOR(i,m,n) for(ll (i) = ((ll) m); (i) < ((ll) n); ++(i))
#define RFOR(i,m,n) for(ll (i) = ((ll) (m)-1); (i) >= ((ll) n); --(i))
#define REP(i,n) FOR(i,0,n)

// i/o
#define TFOUT(b,t,f) cout << ((b)? (t) : (f)) << endl

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
    int N;
    cin>>N;
    vector<ll> A;
    REP(i,N){
        ll tmp; cin>>tmp;
        A.PB(tmp);
    }
    ll truesum = accumulate(A.begin(), A.end(), 0);

    REP(m_fixed, max(A[0],A[A.size()-1])){
        if(m_fixed%2!=0) continue;
        bool f = false;
        vector<ll> mm;
        mm.PB(m_fixed);
        ll tmpsum = 0;
        // ll ba = A[-1] - m_fixed/2;
        ll a = A[0] - m_fixed/2;
        FOR(i, 1, N){
            mm.PB(a*2);
            tmpsum += mm[i];
            if(A[i] < a){
                f = true;
                break;
            }
            a = A[i] - a;
        }
        if(f || truesum != tmpsum) continue;
        cout<<mm[0];
        FOR(i,1,N){
            cout<<" "<<mm[i];
        }
        cout<<endl;
        break;
    }

    return 0;
}
