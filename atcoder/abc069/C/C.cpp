#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    long long int N, a, b=0, c=0;
    cin >> N;
    for(long long int i = 0; i < N; i++){
        cin>>a;
        if(a%4==0) b++; //4の倍数
        else if(a%2==0) c++; //2の倍数
    }
    a = c>=2 ? (N-c-4)/4+2 : N/4+1;
 
    if(N==c || N==b+c) cout << "Yes" << endl;
    else if (b!=0 && N==b+c+1) cout << "Yes" << endl;
    else cout << ((a<=b) ? "Yes" : "No") << endl;
 
    return 0;
}