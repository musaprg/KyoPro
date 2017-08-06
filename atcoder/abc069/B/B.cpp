#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string s;
    cin >> s;
    cout << s.front() << s.size()-2 << s.back() << endl;
    return 0;
}