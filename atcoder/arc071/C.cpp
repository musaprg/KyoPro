#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

#define SIZEOFALP 26

using namespace std;

int main(){
    int n,i,j,k,ans;
    string stin;
    cin>>n;
    vector< vector<int> > snum (n, vector<int>(SIZEOFALP));
    vector<int> num (SIZEOFALP);
    string S;
    for (i = 0; i < n; ++i) {
        cin>>S;
        for (j = 0; j < S.size(); ++j) {
            printf("%d\n", (int)(S[j])-97);
            snum[i][(int)(S[j])-97]++;
        }
    }
    for (i = 0; i < SIZEOFALP; ++i) {
        for (j = 0; j < n; ++j) {
            num[i] = snum[j][i];
        }
        ans = *min_element(num.begin(), num.end());
        printf("Ans: %d\n", ans);
        for(k = 0; k < ans; k++){
            printf("%d", i+97);
        }
    }
    printf("\n");
    return 0;
}
