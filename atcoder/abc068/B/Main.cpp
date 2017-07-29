#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N,ansc=0,ans=1;
    cin >> N;
    for(int i = 1; i<=N; i++){
        if(i%2!=0) continue;
        int t = i;
        int c = 0;
        for(;;){
            if(t%2!=0) break;
            t/=2;
            c++;
        }
        if(ansc<c){
            ans=i;
            ansc=c;
        }
    }
    cout<<ans<<endl;
    return 0;
}