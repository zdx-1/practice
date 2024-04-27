#include <iostream>
using namespace std;

const int M = 1e5 + 10, N = 1e7 + 10;
int n, a[M];
long res;
long q1[N], q2[N];
int hh1, tt1, hh2, tt2;

// 快读
void read(int &x) {
  int si = 1;
  x = 0;
  char c = getchar();
  if (c == '-') si = -1, c = getchar();
  for (; '0' <= c && c <= '9'; c = getchar())
    x = x * 10 + c - '0';
  x *= si;
}

// 两个队列里取队头最小值
long find_min() {
  long x;
  if (hh2 == tt2 || hh1 < tt1 && q1[hh1] < q2[hh2]) x = q1[hh1++];
  else x = q2[hh2++];
  return x;
}

int main() {
  read(n);
  for (int i = 1, x; i <= n; i++) {
    read(x);
    a[x]++;
  }

  for (int i = 1; i < M; i++) while (a[i]) a[i]--, q1[tt1++] = i;
  for (int i = 1; i < n; i++) {
    long x = find_min(), y = find_min();
    res += x + y;
    q2[tt2++] = x + y;
  }

  printf("%ld\n", res);
}