#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

//color
#define NOCOLOR 0
#define BLACK 1 //Fennec
#define WHITE 2 //Snuke
#define N 22222

using namespace std;

int n, M[N][N];
int color[N];

void bfs(int s1, int s2, int turn){
    queue<int> q1;
    queue<int> q2;
    q1.push(s1); //init state(fennec)
    q2.push(s2); //init state(snuke)
    for(int i = 0; i < n; i++) color[i]=NOCOLOR;
    color[0]=BLACK;
    color[n-1]=WHITE;
    int u1,u2;
    while(!q1.empty() && !q2.empty()){
        if(turn==0){
            // cout<<"Fennec's Turn"<<endl;
            u1=q1.front(); q1.pop();
            for(int v = 0; v < n; v++){
                if(M[u1][v]==0) continue;
                if(color[v]!=NOCOLOR) continue;
                color[v] = BLACK;
                // cout<<"proceed"<<v<<endl;
                q1.push(v);
            }
            turn=1;//next snuke
        }else{
            // cout<<"Snuke's Turn"<<endl;
            u2=q2.front(); q2.pop();
            for(int v = 0; v < n; v++){
                if(M[u2][v]==0) continue;
                if(color[v]!=NOCOLOR) continue;
                color[v] = WHITE;
                // cout<<"proceed"<<v<<endl;
                q2.push(v);
            }
            turn=0;//next fennec
        }
    }
    if(!q1.empty()){
        cout<<"Fennec"<<endl;
    }else{
        cout<<"Snuke"<<endl;
    }
}

int main(void){
    cin.sync_with_stdio(false);
    int a,b;
    cin>>n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            M[i][j] = 0;
        }
    }
    for(int i = 0; i < n-1; i++){
        int a,b;
        cin>>a>>b;
        a--; b--;
        M[a][b]=1;
        M[b][a]=1;
    }

    bfs(0,n-1,0);
    return 0;
}