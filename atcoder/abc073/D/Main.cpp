#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#define ll long long int
#define MAX 201
#define INF (1<<21)

using namespace std;

int N,M,R;
set<int> rs;
int W[MAX][MAX];
int d[MAX][MAX];

// void dij(){
//     int minv;
//     int d[MAX];     //d:dist
//     int s[MAX];     //s:state

//     for(int i = 1; i <= N; i++){
//         d[i] = INF; s[i] = 0;
//     }

//     d[*rs.begin()] = 0; s[*rs.begin()] = 1;
//     // cout<<*rs.begin()<<endl;

//     for(;;){
//         minv = INF;
//         int u = -1;
//         for(auto i : rs){
//             if(minv > d[i] && s[i] != 2){
//                 u = i;
//                 minv = d[i];
//             }
//         }
//         if(u==-1) break;
//         s[u] = 2; //reached
//         for(auto v : rs){
//             if(s[v]==0 && W[u][v] != INF){
//                 if(d[v]>d[u]+W[u][v]){
//                     d[v] = d[u]+W[u][v];
//                     s[v] = 1;
//                 }
//             }
//         }
//     }
//     cout<<d[N]<<endl;
// }

void dij(int b){
    int minv;
    int s[MAX];     //s:state

    for(int i = 1; i <= N; i++){
        d[b][i] = INF; s[i] = 0;
    }

    d[b][b] = 0; s[b] = 1;

    for(;;){
        minv = INF;
        int u = -1;
        for(int i = 1; i <= N; i++){
            if(minv > d[b][i] && s[i] != 2){
                u = i;
                minv = d[b][i];
            }
        }
        if(u==-1) break;
        s[u] = 2; //reached
        for(int v = 1; v <= N; v++){
            if(s[v]==0 && W[u][v] != INF){
                if(d[v]>d[u]+W[u][v]){
                    d[b][v] = d[b][u]+W[u][v];
                    s[v] = 1;
                }
            }
        }
    }
}

void solve(){
    
}

int main(void){
    cin.sync_with_stdio(false);
    cin>>N>>M>>R;
    for(int i = 1; i <= N; i++){
        for(int k = 1; k <= N; k++){
            W[i][k] = INF;
        }
    }
    for(int i = 0; i < R; i++){
        int r; cin>>r;
        rs.insert(r);
    }
    for(int i = 0; i < M; i++){
        int a,b,c; cin>>a>>b>>c;
        W[a][b] = c;
    }
    for(int i = 1; i <= N; i++){
        dij(i);
    }

    return 0;
}