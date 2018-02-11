#include <iostream>
#include <vector> //可変長配列
#include <queue> //キュー
#include <unordered_map> //ハッシュ連想配列
#include <numeric>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#define ll long long int
#define INFTY (1<<21)

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    for(;;){
        int N; cin>>N;
        if(N==0) break;
        int imat[2] = {10, 10};
        int gems[20][2];
        bool iscatched[20];
        for(int i = 0; i < N; i++){
            iscatched[i] = false;
        }
        for(int i = 0; i < N; i++)
            cin>>gems[i][0]>>gems[i][1];
        int M; cin>>M;
        for(int i = 0; i < M; i++){
            char dir; cin>>dir;
            int distance; cin>>distance;
            cout<<dir<<" "<<distance<<endl;
            switch(dir){
                case 'N': //y+
                    cout<<"N"<<endl;
                    for(int j = 0; j < N; j++){
                        if(iscatched[j]) continue;
                        if(imat[1]<=gems[j][1] && gems[j][1]<=imat[1]-distance && imat[0]==gems[j][0])
                            iscatched[j] = true;
                    }
                    imat[1] -= distance;
                    break;
                case 'E': //x+
                    cout<<"E"<<endl;
                    for(int j = 0; j < N; j++){
                        if(iscatched[j]) continue;
                        if(imat[0]>=gems[j][0] && gems[j][0]>=imat[0]+distance && imat[1]==gems[j][1])
                            iscatched[j] = true;
                    }
                    imat[0] += distance;
                    break;
                case 'S': //y-
                    cout<<"S"<<endl;
                    for(int j = 0; j < N; j++){
                        if(iscatched[j]) continue;
                        if(imat[1]>=gems[j][1] && gems[j][1]>=imat[1]+distance && imat[0]==gems[j][0])
                            iscatched[j] = true;
                    }
                    imat[1] += distance;
                    break;
                case 'W': //x-
                    cout<<"W"<<endl;
                    for(int j = 0; j < N; j++){
                        if(iscatched[j]) continue;
                        if(imat[0]<=gems[j][0] && gems[j][0]<=imat[0]-distance && imat[1]==gems[j][1])
                            iscatched[j] = true;
                    }
                    imat[0] -= distance;
                    break;
            }
            cout<<imat[0]<<","<<imat[1]<<endl;
        }
        bool isend = false;
        for(int i = 0; i < N; i++){
            if(!iscatched[i]){
                cout<<"No"<<endl;
                isend = true;
                break;
            }
        }
        if(!isend) cout<<"Yes"<<endl;
    }
    return 0;
}