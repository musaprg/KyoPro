#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string s; cin>>s;
    for(int i = 0; i < s.size(); i+=2){
        cout<<s[i];
    }
    cout<<endl;
    return 0;
}