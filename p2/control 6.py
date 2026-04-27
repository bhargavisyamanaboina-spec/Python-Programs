mylist=input("Enter a list of numbers separated by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum+=num
    print("The sum of the numbers is:",sum)
