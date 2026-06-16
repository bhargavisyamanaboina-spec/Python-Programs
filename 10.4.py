try:
  file=open("myfile.txt","r")
except toError:
  print("Error:unable to read the file!")
finally:
   file.close()
