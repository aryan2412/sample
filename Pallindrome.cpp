#include<stdio.h>
#include<conio.h>
main()
{
int n,temp,rev=0,r;
printf("enter a number");
scanf("%d",&n);
temp=n;
while(temp>0)
{
r=temp%10;
rev=(rev*10)+r;
temp=temp/10;
}
if(n==rev)
{
printf("%d is a pallindrome number",n);
}
else
{
printf("%d is not a pallindrome number",n);
}
getch();
}

