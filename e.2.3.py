import re
text="Devops123"
if re.match(r'^[A-za-z0-9]+$',text):
      print("Alphanumeric string")
else:
      print("Not Alphanumeric")
