import subprocess as sb
import re

web = input("Enter a website name : ")
print("Looking for address...")
output = sb.run(
    ["host", web],
    capture_output=True,
    text=True,
    )
result = re.search(r'has address (\d+\.\d+\.\d+\.\d+)', output.stdout)
if result:
    ipadd = result.group(1)
    print(web, "ip address :", ipadd)
    print("Scanning for open ports and server details...")
    output = sb.run(
        ["nmap", "-T5", "-sV", ipadd],
        capture_output=True,
        text=True,
    )
    print(output.stdout)
else:
    print("Could not find an IPv4 address.")
