#include<stdio.h>
#include <math.h>
#include <iostream>
#include <iomanip>
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
    // // 三整数排序
    // int a,b,c,t;
    // cin>>a>>b>>c;
    // if(a>b){t=a;a=b;b=t;}
    // if(a>c){t=a;a=c;c=t;}
    // if(b>c){t=b;b=c;c=t;}
    // cout<<a<<" "<<b<<" "<<c<<endl;

    /*1.5 注解和习题*/
    //实验A1：表达式11111*11111的值是多少？把5个1改成6个1呢？9个1呢？
    //cout<<11111*11111<<endl;// 1234534321

    //实验A2：把实验A1中的所有数换成浮点数，结果如何？
    //cout<<11111.0*11111.0<<endl;// 1.23454e+08

    //实验A3：表达式sqrt（-10）的值是多少？尝试用各种方式输出。在计算的过程中系统会报错吗？
    //cout<<sqrt(-10)<<endl;// nan
    // cout<<"sqrt(-10)="<<sqrt(-10)<<endl;
    // cout<<"sqrt(-10)="<<sqrt(-10.0)<<endl;
    // cout<<"sqrt(-10)="<<sqrt(-10.0f)<<endl;
    // cout<<"sqrt(-10)="<<sqrt(-10.0l)<<endl;

    // //实验A4：表达式1.0/0.0、0.0/0.0的值是多少？尝试用各种方式输出。在计算的过程中系统会报错吗？
    // cout<<1.0/0.0<<endl; // inf
    // cout<<0.0/0.0<<endl; // nan

    //实验A5：表达式1/0的值是多少？在计算的过程中系统会报错吗？
    //cout<<1/0<<endl; // Arithmetic exception

    // //实验B1：在同一行中输入12和2，并以空格分隔，是否得到了预期的结果？
    // int a,b;
    // cin>>a>>b;
    // cout<<a/b<<endl; // 6 正常

    // //实验B2：在不同的两行中输入12和2，是否得到了预期的结果？
    // int a,b;
    // cin>>a;
    // cin>>b;
    // cout<<a/b<<endl; // 6 正常

    // // 实验B3：在实验B1和B2中，在12和2的前面和后面加入大量的空格或水平制表符（TAB），甚至插入一些空行。
    // int a,b;
    // cin>>a>>b;
    // cout<<a/b<<endl;// 6 正常

    // //实验B4：把2换成字符s，重复实验B1～B3。
    // char s;
    // cin>>s;
    // cout<<s/s<<endl; // 1 正常

    /*习题*/
    // // 平均数
    // int a,b,c;
    // cin>>a>>b>>c;
    // //保留三位小数
    // //cout输出控制小数位，需要添加头文件#include <iomanip>
    // cout<<setiosflags(ios::fixed)
    //     <<setprecision(3)<<(a+b+c)/3.0<<endl;
    // // 温度
    // double f,c;
    // cin>>f;
    // c=(f-32)*5/9;
    // cout<<setiosflags(ios::fixed)
    //     <<setprecision(3)<<c<<endl;
    // // 连续和
    // // 输入正整数n，输出1到n的连续和。
    // int n,m;
    // cin>>n;
    // m=n*(n+1)/2;
    // cout<<m<<endl;
    // // sin和cos
    // int n;
    // cin>>n;
    // cout<<sin(n)<<" "<<cos(n)<<endl;
    // // 打折
    // double price,discount,total;
    // cin>>discount;
    // price=95;
    // total=price*discount;
    // if (total>=300)
    // {
    //     cout<<"Total price is "<<total*0.85<<" yuan."<<endl;
    // }else{
    //     cout<<"Total price is "<<total<<" yuan."<<endl;
    // }
    // // 三角形
    // int a,b,c;
    // cin>>a>>b>>c;
    // if (a+b>c && a+c>b && b+c>a)
    // {
    //     cout<<"Yes"<<endl;
    // }else{
    //     cout<<"No"<<endl;
    // }
    // // 年份
    // int year;
    // cin>>year;
    // if (year%400==0 || (year%4==0 && year%100!=0))
    // {
    //     cout<<"Yes"<<endl;
    // }else{
    //     cout<<"No"<<endl;
    // }

    // //问题1：int型整数的最小值和最大值是多少（需要精确值）？
    // cout<<INT_MIN<<" "<<INT_MAX<<endl;// -2147483648 2147483647
    // //问题2：double型浮点数能精确到多少位小数？或者，这个问题本身值得商榷？
    // cout<<DBL_DIG<<endl;// 15
    // //问题3：double型浮点数最大正数值和最小正数值分别是多少（不必特别精确）？
    // cout<<DBL_MIN<<" "<<DBL_MAX<<endl;// 2.22507e-308 1.79769e+308
    // //问题4：逻辑运算符号“&&”、“||”和“！”（表示逻辑非）的相对优先级是怎样的？也就是说，a&&b||c应理解成（a&&b）||c还是a&&（b||c），或者随便怎么理解都可以？
    //  cout<<"&&优先级高于||"<<endl;
    //  cout<<"!优先级最低"<<endl;
    //  cout<<"a&&b||c"<<endl;
    //  cout<<"(a&&b)||c"<<endl;
    //  cout<<"a&&(b||c)"<<endl;
    // // 问题5：if（a）if（b）x＋＋；else  y＋＋的确切含义是什么？这个else应和哪个if配套？有没有办法明确表达出配套方法？
    // int a,b,x,y;
    // a=1,b=1,x=0,y=0;
    // if(a)if(b)x++;else y++;
    // cout<<a<<" "<<b<<endl;
    system("pause");
    return 0;
}