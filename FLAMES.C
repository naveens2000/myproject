#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    char str[100]={'f','l','a','m','e','s'};
    char str2[100],str1[100],str3[100],str4[100];
    char flames;
    int m1,f1,x,i,l,n=0,k,j=0,m=0,f,count=0,max=0;
    clrscr();
    printf("\n***************************************************");
    printf("\n|         __        __    __  __    __   __       |");
    printf("\n|        |__  |    |__|  |  \/  |  |__  |__       |");
    printf("\n|        |    |__  |  |  |      |  |__   __|      |");
    printf("\n***************************************************");
    printf("\nENTER THE MALE NAME:");
    scanf("%[^\n]s",str1);
    printf("\nENTER THE FEMALE NAME:");
    scanf("%s",str2);
    strcpy(str3,str1);
    strcpy(str4,str2);
     m1=strlen(str1);
     f1=strlen(str2);
    for(m=0;m<m1;m++)
    {  f=0;
	while(f<f1){
	if(str1[m]==str2[f])
	{
	    str1[m]='\0';
	    str2[f]='\0';
	    break;
	}
	else
	{
	    f++;
	}
    }
    }
    max=(m1>f1)?m1:f1;
    for(x=0;x<max;x++)
    {
	if(str1[x]!='\0')
	    n=n+1;
	if(str2[x]!='\0')
	    n=n+1;
    }
    k=n;
    for(i=0;i<5;i++)
    {
	while(j<6)
	{
	    if(str[j]!='\0')
	    {
		if(count!=k-1)
		{
		    count++;
		    j++;
		    if(j==6)
		    {
			j=0;
		    }

		}
	       else
	       {
		   str[j]='\0';
		   count=0;
		   j++;
		   if(j==6)
		   {
		       j=0;
		   }
		   break;
	      }
	   }
	   else
	   {
	       j++;
	       if(j==6)
	       {
		  j=0;
	       }
	  }
       }

    }
    for(l=0;l<6;l++)
    {
	if(str[l]!='\0'){
	    flames=str[l];
	}
	}
  switch(flames)
  {
      case 'f':printf("hai %s and %s you both are meant to be the best friends",str3,str4);
      break;
      case 'l':printf("hai %s and %s you both are meant to be lovers and made for each others",str3,str4);
      break;
      case 'a':printf("hai %s and %s you both are meant to be affectionate to each others",str3,str4);
      break;
      case 'm':printf("hai %s and %s you both are meant gonna be married",str3,str4);
      break;
      case 'e':printf("hai %s and %s you both are meant to be enemies",str3,str4);
      break;
      case 's':printf("hai %s and %s you both are meant to be brother or sister for each other",str3,str4);
      break;
      default:
	break;
  }
  getch();
  return 0;
}
