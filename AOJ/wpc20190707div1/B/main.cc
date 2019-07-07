#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

#define FOR(i, a, n) for(ll i = ((ll) a); i < ((ll) n); ++i)
#define REP(i, n) FOR(i, 0, n)

#define DMP(x) cerr << #x << " = " << (x) << endl;
#define DBG(x) cerr << #x << " = " << (x) << " (L" << __ LINE__ << ") " << " " << __FILE__ << endl;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<long long> vll;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

inline bool is_in(const ll y, const pll p) {
    return p.first <= y && y <= p.second;
}

int main() {
    while(true) {
        int n, q;
        cin >> n >> q;
        if(n == 0 && q == 0) break;
        unordered_map<string, pll> hs;
        REP(i, n) {
            string en;
            ll ey, wy;
            cin >> en >> ey >> wy;
            hs[en] = make_pair(wy - ey + 1, wy);
        }
        REP(i, q) {
            ll qy;
            cin >> qy;
            bool find_flg = false;
            for(auto v : hs) {
                if(is_in(qy, v.second)) {
                    cout << v.first << " " << qy - v.second.first + 1 << endl;
                    find_flg = true;
                    break;
                }
            }
            if(!find_flg) cout << "Unknown" << endl;
        }
    }
    return 0;
}