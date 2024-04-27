#include<stdio.h>
int main()
{
    int l = 0, m = 0;//马路长度和区间个数
    scanf("%d%d", &l, &m);
    int u = 0, v = 0;//区间的左右位置，u肯定小于v滴
    int tree[10001]={0};
    //树树全部初始化为0，代表没砍过
    for (int i = 0; i < m; i++)//一共有m个区间，那就得操作m次呐
    {
        scanf("%d%d", &u, &v);//想从哪砍到哪呢
        for (int j = u; j <= v; j++)
        {
            if(tree[j]==0)
            tree[j] = 1;//砍过的标记为1
        }
    }
    int sum = 0;//剩余sum棵树树还没被砍
    for (int k = 0; k <= l; k++)//遍历树树
    {
        if (tree[k] == 0) sum++;
    }
    printf("%d", sum);
    return 0;
}