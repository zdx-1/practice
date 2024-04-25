每一行都是新的，前面的值会被覆盖，所以不用判断，硬要判断是这样的。
```cpp
#include <iostream>
#include <cstdio>
using namespace std;
int x[15] = {0};
int sum, n;

int PD(int k)
{

    for (int i = 1; i < k; i++)
    {
        if (abs(k - i) == abs(x[k] - x[i]))
            return 0;
        else if (x[k] == x[i])
            return 0;
        // 即判断是否符合条件来放,i表示皇后所在的行数，x[i]表示所在的列数，
        // 所以前面那个条件用来判断两个皇后是否在对角线上,后面用来判断是否在同一列上。
        // 行数不需要判断，因为他们本身的i就代表的是行数
    }
    return 1;
}

bool check(int a)
{

    if (a > n)
        sum++;
    else
        return 0;
    return 1;
}

void DFS(int a)
{
    if (check(a))
        return;
    else
        for (int i = 1; i <= n; i++)
        {
            if (x[a] != 0)
                continue; // 当前位置已被放过
            x[a] = i;     // 标记使用
            if (PD(a))
                DFS(a + 1);
            // 判断是否能放这步

            // 能的话进行下一个皇后的放置

            x[a] = 0;

            // 不能就下一列
        }
}
int main()
{
    cin >> n;
    // 表示几个皇后
    DFS(1);
    // 每次都从第一个皇后开始
    cout << sum << endl;
    return 0;
}
```
```python
x = [0] * 15
n = 0
sum = 0
def pd(k):
    for i in range(1, k):
        if abs(k - i) == abs(x[k] - x[i]):
            return 0
        elif x[k] == x[i]:
            return 0
        # 即判断是否符合条件来放,i表示皇后所在的行数，x[i]表示所在的列数，
        # 所以前面那个条件用来判断两个皇后是否在对角线上,后面用来判断是否在同一列上。
        # 行数不需要判断，因为他们本身的i就代表的是行数
    return 1

def check(a):
    if a > n:
        global sum
        sum += 1
    else:
        return False
    return True


def DFS(a):

    if check(a):
        return
    else:
        for i in range(1, n + 1):

            if x[a]!=0: continue
            x[a] = i
            # 第a个皇后放的列数
            if pd(a):
                # 判断是否能放这步
                DFS(a + 1)
                # 能的话进行下一个皇后的放置
            x[a] = 0

                #   不能就下一列

if __name__ == '__main__':

    n = int(input())
    # 不能就下一列
    DFS(1)
    # 每次都从第一个皇后开始
    print(sum)
```
```java
import java.util.Scanner;
import static java.lang.Math.abs;
public class Main {
    static int x[] = new int[15];
    static int sum, n;
    static boolean PD(int k) {
        for (int i = 1; i < k; i++) {
            if (abs(k - i) == abs(x[k] - x[i]))
                return false;
            else if (x[k] == x[i])
                return false;
            //即判断是否符合条件来放,i表示皇后所在的行数，x[i]表示所在的列数，
            //所以前面那个条件用来判断两个皇后是否在对角线上,后面用来判断是否在同一列上。
            //行数不需要判断，因为他们本身的i就代表的是行数

        }
        return true;
    }

    static boolean check(int a) {

        if (a > n)
            sum++;
        else
            return false;
        return true;
    }

    static void DFS(int a) {
        if (check(a))
            return;
        else
            for (int i = 1; i <= n; i++) {
                if (x[a]!=0)
                    continue;
                x[a] = i;
                //第a个皇后放的列数
                if (PD(a))
                    //判断是否能放这步
                    DFS(a + 1);
                    //能的话进行下一个皇后的放置
                x[a]=0;
                //不能就下一列
            }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        //表示几个皇后
        DFS(1);
        //每次都从第一个皇后开始
        System.out.println(sum);
    }
}
```
