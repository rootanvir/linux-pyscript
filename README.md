```python
import subprocess as sb
import re
web = input("Enter a website name : ")
print("Looking for address...")
output = sb.run(
    ["host",web],
    capture_output=True,
    text=True,
)
result = re.search(r'has address (\d+\.\d+\.\d+\.\d+)',output.stdout)
print(web," ip address : ",result.group(1))
ipadd = result.group(1)
print("Scaning for open port...")
output = sb.run(
    ["nmap","-T4",ipadd],
    capture_output=True,
    text=True,
)
print(output.stdout)
```
