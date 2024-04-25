#include<stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
//算数表达式的计算

int main()
{
    /* 算术表达式的计算 */
    // printf("%d\n",1+2);
    // //实验一
    // printf("%d\n",3-4);
    // //二
    // printf("%d\n",5*6);
    // //三
    // printf("%d\n",7/8);
    // //四
    // printf("%d\n",9%10);
    // //五
    // printf("%.1f\n",8.0/5.0);
    // //整数值用%d,浮点数用%f
    // //比较复杂的表达式计算
    // printf("%.8f\n",1+2*sqrt(3)/(5-0.1));
    // //数学函数sqrt(x)的作用是计算x的算术平方根
    // printf("%.8f\n",pow(2,3));
    // //pow(x,y)的作用是计算x的y次方


    /* 1.2 输入输出 */
    // int a,b;
    // scanf("%d%d",&a,&b);
    // printf("%d\n",a+b);
    // 输入的样例
    // //例题1-1 圆柱体的表面积
    // const double PI=acos(-1.0);
    // double r,h,s1,s2,s;
    // //cin>>r>>h;
    // scanf("%lf%lf",&r,&h);
    // s1=2*PI*r*r;
    // s2=2*PI*r*h;
    // s=s1+s2;
    // printf("Area=%.3f\n",s);
    // cout << "" << endl;
    //算法竞赛的程序应当只做3件事情：
    //读入数据、计算结果、打印输出。
    //尽量使用const关键字声明常数


    /*1.3 顺序结构程序设计*/
    // //三位数翻转
    // int a,b,c;
    // cin>>a>>b>>c;
    // cout<<c<<b<<a<<endl;
    // // 交换变量
    // // 三变量法
    // int a,b,c;
    // cin>>a>>b;
    // c=a;
    // a=b;
    // b=c;
    // cout<<a<<" "<<b<<endl;
    // // 两变量法
    // int a,b;
    // cin>>a>>b;
    // a=a+b;
    // b=a-b;
    // a=a-b;
    // cout<<a<<" "<<b<<endl;
    // // 输入输出
    // int a,b;
    // cin>>a>>b;
    // cout<<b<<" "<<a<<endl;

    /*1.4 分支结构程序设计*/
    // //鸡兔同笼
    // int a,b,n,m;
    // cin>>n>>m;
    // if(n>m){cout<<"No answer"<<endl;}
    // else{
    //     a=(4*n-m)/2;
    //     b=n-a;
    //     if (m%2==1 || a<0 || b<0)
    //     {
    //         cout<<"No answer"<<endl;
    //     }
    //     else{
    //         cout<<a<<" "<<b<<endl;
    //     }
    // }
    // //C语言中的逻辑运算符都是短路运算符
    // //&&和||都是短路运算符，当第一个运算符为假时，第二个运算符将不会被执行。
    // 三整数排序
    int a,b,c,t;
    cin>>a>>b>>c;
    if(a>b){t=a;a=b;b=t;}
    if(a>c){t=a;a=c;c=t;}
    if(b>c){t=b;b=c;c=t;}
    cout<<a<<" "<<b<<" "<<c<<endl;
    system("pause");
    return 0;
}