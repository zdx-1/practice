#include <bits/stdc++.h>
 
using namespace std;
 
int a[105]; // 标记
 
int main()
{
    int i,j;
    string s;
    cin >> s;
    for (i=0; i<s.length(); i++) {
        if (s[i] == ')') { // 找到了右括号
            for (j=i-1; j>=0; j--) {
                if (s[j] == '(' and a[j] == 0) { // 找到了没被匹配过的左括号且匹配成功
                    a[i] = a[j] = 1;
                    break;
                }
                else if (s[j] == '[' and a[j] == 0) break; // 找到了左括号但匹配失败
            }
            // 找不到左括号，不做任何操作
        }
        // 下面同理
        else if (s[i] == ']') {
            for (j=i-1; j>=0; j--) {
                if (s[j] == '[' and a[j] == 0) {
                    a[i] = a[j] = 1;
                    break;
                }
                else if (s[j] == '(' and a[j] == 0) break;
            }
        }
    }
    for (i=0; i<s.length(); i++) {
        if (a[i] == 0) { // 没有匹配则成对输出
            if (s[i] == '(' or s[i] == ')') cout << "()";
            else cout << "[]";
        }
        else cout << s[i]; // 匹配成功则直接输出
    }
    return 0;
}