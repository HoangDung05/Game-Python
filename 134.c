#include<stdio.h>

int main(int argc, char const *argv[])
{
    int n, count = 0, i;
    int a[32];
    scanf("%d", &n);
    while (n > 0)
    {
        a[count] = n % 2;
        n/=2;
        count++;
    }
    
    for(i = count-1; i >= 0; i--)
    {
        printf("%d", a[i]);
    }
    
    return 0;
}
