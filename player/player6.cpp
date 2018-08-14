#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	string a;
	cin>>a;
	int i,n=0;
	char temp;
	for(i=0;a[i]!='\0';i++)
		n++;
	for(i=0;i<n;i=i+2)
	{
		temp = a[i];
		a[i] = a[i+1];
		a[i+1] = temp;  
	}	
	cout<<a;
}
