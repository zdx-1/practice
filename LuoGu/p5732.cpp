# include <stdio.h>
int main ()
{
	int n;
	scanf("%d",&n);
	int arr[30][30]={0};
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=i;j++)
		{
			if(i==1&&j==1)
			{
				arr[1][1]=1;
				printf("%d ",arr[i][j]);     //第一行是特殊的，需要注意
				break;
			}
			arr[i][j]=arr[i-1][j-1]+arr[i-1][j];
			printf("%d ",arr[i][j]);
		}
		printf("\n");
	}
}