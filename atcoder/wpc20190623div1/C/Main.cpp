#include <bits/stdc++.h>

using namespace std;

int main(void) {
    while(true) {
        int n, m;
        cin >> n >> m;
        if(n == 0 && m == 0) break;
        vector<int> win(n, 0), lose(n, 0);
        for(int i = 0; i < m; i++) {
            int s, k;
            cin >> s >> k;
            if(k == 1) {
                int c;
                cin >> c;
                lose[c - 1] += s;
                win[c - 1] += s;
            }
            else {
               for(int j = 0; j < k; j++) {
                   int c;
                   cin >> c;
                   win[c - 1] += s;
                }
            }
        }
    
        int fmin = INT_MAX, smin = INT_MAX;
        for(int i = 0; i < n; i++) {
            if(fmin > lose[i]) {
                smin = fmin;
                fmin = lose[i];
            }
            else if(smin > lose[i]) smin = min(smin, lose[i]);
        }
        int ans = -1;
        for(int i = 0; i < n; i++) {
            int diff = win[i] - (lose[i] == fmin ? smin : fmin);
            ans = max(ans, diff + 1);
        }
            cout << ans << "\n";
    }
    return 0;
}
