#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#define ll long long int

using namespace std;

int H,W;
int numquad,numduo,numuno;
int ctbl[26];

int rec(){
    //ここでDPすればいける
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>H>>W;
    for(int i = 0; i < 26; i++){
        ctbl[i] = 0;
    }
    getchar();
    for(int i = 0; i < H; i++){
        for(int k = 0; k < W; k++){
            char c; c = getchar();
            ctbl[c-'a']++;
        }
        getchar();
    }
    // for(int i = 0; i < 26; i++){
    //     cout<<ctbl[i]<<endl;
    // }
    numquad = (H/2) * (W/2);
    numduo = (W/2)*(H%2) + (H/2)*(W%2);
    numuno = (H%2+W%2)/2;
    // cout << numquad << endl;
    // cout << numduo << endl;
    // cout << numuno << endl;
    return 0;
}