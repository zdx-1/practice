//P1449
#include <iostream>
#include <stack>
using namespace std;
stack <int> n;
int s=0;
int main(){
    char ch;
    while(1){
        cin>>ch;
        if(ch<='9'&&ch>='0') s=s*10+ch-'0';//累计
        else if(ch=='.'){
            n.push(s);//压栈
            s=0;//s清零
        }
        else if(ch!='@'){
            int a1=n.top();n.pop();int a2=n.top();n.pop();//弹出栈顶两个元素
            if(ch=='+') n.push(a1+a2);
            if(ch=='-') n.push(a2-a1);
            if(ch=='*') n.push(a1*a2);
            if(ch=='/') n.push(a2/a1);
            //压入结果
        }
        else break;
    }
    cout<<n.top();
    return 0;
}