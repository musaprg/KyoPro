#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    string w; char c;
    while((c = getchar()) != EOF){
        if(c=='\n') continue;
        if(c!='a'&&c!='i'&&c!='u'&&c!='e'&&c!='o') w+=c;
    }
    cout<<w<<endl;
    return 0;
}