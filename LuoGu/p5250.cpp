#include<bits/stdc++.h>
using namespace std;
#define IOS ios::sync_with_stdio(0),cin.tie(0),cout.tie(0)
#define endl "\n"
#define int long long
#define pb push_back
#define lb lower_bound
#define ub upper_bound
const int INF = 1e12+10;
set<int> s;//存放木材 
int num=0;//目前有几个木材 
void solve(){
	int op,x;
	cin>>op>>x;
	if(op==1){
		if(s.count(x))
		  cout<<"Already Exist"<<endl;
		else
		  s.insert(x);//存放长度为x木材  
	}else if(op==2){
		if(s.size()==2)
		  cout<<"Empty"<<endl;
		else {
			auto k=s.lb(x);
			if(*k==x){//有刚好长度的木材 
				cout<<x<<endl;
				s.erase(k);
			}else{
				auto k1=s.lb(x),k2=--s.lb(x);//找到长度接近x的木材 
				if(abs(*k1-x)<abs(*k2-x)){ 
					cout<<*k1<<endl;
					s.erase(k1); 
				}else{//取最接近x且比较短的一根木材
					cout<<*k2<<endl;
					s.erase(k2); 
				}
			}
		}
	} 
}
signed main(){
	IOS;
	s.insert(INF),s.insert(-INF);
	int T=1;
	cin>>T;
	while(T--){
		solve();
	}
	return 0;
}
