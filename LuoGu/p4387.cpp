#include<stdio.h>
#include<string.h>
int a[100005]={0},top=0,b[100005]={0},c[100005]={0};
main()
{
	int i,j=0,k,q,n;
	scanf("%d",&q);
	while(q--)
	{
		scanf("%d",&n);
		memset(a,0,n*4);
		memset(b,0,n*4);
		memset(c,0,n*4);
		for(i=0;i<n;i++)
		scanf("%d",&a[i]);
		for(i=0;i<n;i++)
		scanf("%d",&b[i]);
		i=0;j=0;  top=0;
		while(i<n)
		{
		c[top++]=a[i++];
		while(c[top-1]==b[j] ){
			j++,top--;
			if(top==0)break;
		}
			
		}
		if(top==0)printf("Yes\n");
		else printf("No\n");
	}
}