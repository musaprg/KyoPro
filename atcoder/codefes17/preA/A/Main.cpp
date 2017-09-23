#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string S; cin>>S;
    cout << (S.substr(0,4) == "YAKI" ? "Yes" : "No") << endl;
    return 0;
}