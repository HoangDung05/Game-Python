#include<stdio.h>
#include<stdbool.h>
#include<math.h>

bool twice(long long n)
{
    int k = n % 10;
    n /= 10;
    while (n >= 10)
    {
        n /= 10;
    }
    if((n / k == 2 && n % k == 0) || (k / n == 2 && k % n == 0)) return 1;
    else return 0;
}

bool check(long long n)
{
    int k = n % 10;
    long long f = n;
    f /= 10;
    long long res = 0;
    int count = 1;
    while (f >= 10)
    {
        res = res * 10 + f % 10;
        f /= 10;
        count++;
    }
    f = f % 10;
    long long g = f * pow(10, count) + res * 10 + k;
    if(g == n) return 1;
    else return 0;
}

void solve()
{
    long long n;
    scanf("%lld", &n);
    if(check(n) && twice(n)) printf("YES\n");
    else printf("NO\n");
}

int main()
{
    int number_test;
    scanf("%d", &number_test);
    while (number_test--)
    {
        solve();
    }
    return 0;
}

