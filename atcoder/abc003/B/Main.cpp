#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string s,n;
    cin>>s>>n;
    bool f = true;
    for(int i = 0; f && i < s.size(); i++){
        if(s[i]!=n[i]){
            if(s[i]=='@' || n[i]=='@'){
                char t = s[i]=='@' ? n[i] : s[i];
                if(t=='a'||t=='t'||t=='c'||t=='o'||t=='d'||t=='e'||t=='r') f=true;
                else f=false;
            }else f=false;
        }else if(s[i]=='@'&&n[i]=='@'){
            f=true; continue;
        }
    }
    if(f) cout<<"You can win"<<endl;
    else cout<<"You will lose"<<endl;
    return 0;
}