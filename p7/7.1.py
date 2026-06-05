def fibonacci(Number):
 if(Number==0):
    return 0
 elif Number==1:
    return 1
 else:
    return fibonacci(Number-2)+fibonacci(Number-1)
Number=int(input("please Enter the Fibonacci Number Range="))
sum=0
for Num in range(Number):
    print(fibonacci(Num),end='')
    sum=sum+fibonacci(Num)
    print("\nThe sum of fibonacci series Numbers=%d"%sum)
