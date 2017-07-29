#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int N, tmp, i;
    unsigned long long sum = 0;
    vector<int> a;
    scanf("%d", &N);
    for(i=0;i<3*N;i++){
        scanf("%d", &tmp);
        a.push_back(tmp);
    }
    sort(a.begin(), a.end());
    auto itr = a.end();
    for(i=0;i<N;i++){
        itr=itr-2;
        sum += *itr;
        
    }
    printf("%lld\n", sum);
    
    return 0;
}
