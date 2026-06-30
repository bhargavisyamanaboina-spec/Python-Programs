import re
text="My phone number is 9876543210"
print(re.findall(r'\d',text))
print(re.findall(r'\d{10}',text))
print(re.match(r'MY',text))
print(re.search(r'phone',text))
