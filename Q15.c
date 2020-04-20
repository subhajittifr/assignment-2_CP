//Question 15

#include<stdio.h>
#include<math.h>
float f(float t,float y) //Defining f(t,y)
{   return(y-pow(t,2)+1);
     }
float f_exact(float t,float y) //Exact analytical solution 
{   return(pow(t+1,2)-0.5*exp(t));
     }
int main()
{
	int i;
	float a=0,b=2,h=0.1;
	int N=(b-a)/h;		//No. of steps
	float y[N+1];
	float t[N+1];
	float y_exact[N+1];
	float error[N+1];
	float err_bound[N+1];
	
	for(i=0;i<N+1;i++)
	{
		y[i]=0;		
		t[i]=a+i*h;	//Mesh points
	}
	
	y[0]=0.5;		//Initial condition
	for(i=0;i<N+1;i++)
	{
		y[i+1]=y[i]+h*f(t[i],y[i]);		//Euler's method
		y_exact[i]=f_exact(t[i],y[i]);	//exact solution
		error[i]=y_exact[i]-y[i];	   //Absolute error
		err_bound[i]=(exp(2)-4)/20*(exp(t[i])-1); //Error bound with using  Lipschitz criterion
	}
	
	printf("No of              Error           Error \n");
	printf("iteration                          bound\n");  // initiation of table
	for(i=0;i<10;i++)
	{
		printf("%d                 %f        %f\n" ,i,y_exact[i],error[i], err_bound[i]);
	}
	for(i=10;i<N+1;i++)
	{
		printf("%d                %f        %f\n" ,i,y_exact[i],error[i], err_bound[i]);
	}
	
	return 0;
}

