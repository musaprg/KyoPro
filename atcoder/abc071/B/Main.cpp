#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    cin.sync_with_stdio(false);
    char c; int a[26];
    for(int i = 0; i < 26; i++){
        a[i] = 0;
    }
    while((c = getchar()) != '\n'){
        a[c-'a']++;
    }
    for(int i = 0; i < 26; i++){
        if(a[i]==0){
            printf("%c\n", i+'a');
            return 0;
        }
    }
    printf("None\n");
    return 0;
}