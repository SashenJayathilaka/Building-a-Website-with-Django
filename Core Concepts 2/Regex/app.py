# Email Address
import re

text = "random String. Myname123@gmail.com . some more random text. Your_Name.8-8-8@Companey.net"

# pattern = re.compile("A random String")
# pattern = re.compile("[ABC]")
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
# pattern = re.compile("@")

# result = pattern.search(text)
result = pattern.findall(text)
print(result)