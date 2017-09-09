#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    cout << (N/10==9 || N%10==9 ? "Yes" : "No") << endl;
    return 0;
}