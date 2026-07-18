import subprocess as sb
web = input("Enter a website name : ")

output = sb.run(
    ["ping","-c","4",web],
    capture_output=True,
    text=True,
)
print(output.stdout)