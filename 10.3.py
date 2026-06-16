try:
   num=int(input("Enter a number:"))
   result=10/num
except valueError:
   print("Error:Invalid input!please enter a valid number:")
except zeroDivisionError:
   print("Error:Division by zero!")
else:
   print("Result:",result)
