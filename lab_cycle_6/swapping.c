
#include<stdio.h>
void main(){
	int a,b;
	printf("enter values a and b");
	scanf("%d %d",&a,&b);
	printf("after swapping");
	a=a+b;
	b=a-b;
	a=a-b;
	printf("\n values a and b is:%d %d",a,b);
}
