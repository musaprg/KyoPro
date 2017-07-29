#include <cstdio>

using namespace std;

int main(int argc, const char * argv[]) {
    int X,i=0;
    scanf("%d", &X);
    while((i*(i+1))/2<X) i++;
    printf("%d\n",i);
    return 0;
}
