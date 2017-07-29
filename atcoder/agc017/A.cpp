#include <iostream>
#include <vector>

using namespace std;

long long int comb(int n, int r)
{
    int i;
    long long int res=1;
    for(i=1;i<=r;i++){
        res=res*(n-i+1)/i;
    }
    return res;
}

int main(void){
    cin.tie(0);
   	ios::sync_with_stdio(false);

    int N,P,odd=0,even=0;
    cin>>N>>P;
    for(int i = 0; i < N; i++){
        int t;
        cin>>t;
        if(t%2==0) even++;
        else odd++;
    }
    vector< vector<long long int> > memo;
    int m = max(even, odd);
    memo.resize(m+1);
    for(int i = 0; i <= m; i++){
        memo[i].resize(m+1);
        for(int j = 0; j <= m; j++)
            memo[i][j] = -1;
    }
    long long int ceven = 0, codd = 0, tmp;
    for(int i = 0; i <= even; i++){ //偶数の組み合わせ
        if(even>=i){
            if(memo[even][i] == -1){
                memo[even][i] = comb(even, i);
                memo[even][even-i] = memo[even][i];
            }
            ceven += memo[even][i];
        }
    }
    if(P==0){
        for(int i = 0; i <= odd; i++){
            int r = i*2;
            if(odd>=r){
                if(memo[odd][r] == -1){
                    memo[odd][r] = comb(odd, r);
                    memo[odd][odd-r] = memo[odd][r];
                }
                codd += memo[odd][r];
            }
        }
    }else{
        for(int i = 0; i <= odd; i++){
            int r = i*2+1;
            if(odd>=r){
                if(memo[odd][r] == -1){
                    memo[odd][r] = comb(odd, r);
                    memo[odd][odd-r] = memo[odd][r];
                }
                codd += memo[odd][r];
            }
        }
    }
    cout<<codd*ceven<<endl;
    return 0;
}