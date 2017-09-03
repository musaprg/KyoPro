#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define MAX 30000

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    int N; cin>>N;
    int start[MAX], end[MAX];
    for(int i = 0; i < MAX; i++){
        start[i]    = -1;
        end[i]      = -1;
    }
    for(int i = 0; i < N; i++){
        string str; cin>>str;
        int l = (int)str.rfind("-"); //loc
        int s = atoi((str.substr(0,l)).c_str());
        int e = atoi((str.substr(l+1,str.size()-l)).c_str());
        
    }
    return 0;
}