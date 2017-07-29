#include <iostream>
#include <vector>
#include <queue>
#define NOCOLOR 0
#define BLACK 1 //Fennec
#define WHITE 2 //Snuke
using namespace std;

int n;
int** M;
int* color;

void bfs(int s1, int s2){
    queue<int> q1,q2;
    q1.push(s1);
    q2.push(s2);
    for(int i = 0; i < n; i++) color[i]=NOCOLOR;
    color[0]=BLACK;
    color[n-1]=WHITE;
    int u1,u2;
    while(!q1.empty() && !q2.empty()){
        u1=q1.front(); q1.pop();
        for(int v = 0; v < n; v++){
            if(M[u1][v]==0) continue;
            if(color[v]!=NOCOLOR) continue;
            color[v] = BLACK;
            q1.push(v);
        }
        u2=q2.front(); q2.pop();
        for(int v = 0; v < n; v++){
            if(M[u2][v]==0) continue;
            if(color[v]!=NOCOLOR) continue;
            color[v] = WHITE;
            q2.push(v);
        }
    }
    if(!q1.empty()) cout<<"Fennec"<<endl;
    else cout<<"Snuke"<<endl;
}
int main(void){
    cin.sync_with_stdio(false);
    int a,b;
    int n;
    cin>>n;
    M = new int*[n];
    color = new int[n];
    for(int i = 0; i < n; i++){
        M[i] = new int[n];
    }
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
    bfs(0,n-1);
    return 0;
}