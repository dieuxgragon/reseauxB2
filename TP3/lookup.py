from socket import gethostbyname

name = input("rentrer le host name ")
ipAddress = gethostbyname(name)
print("ipAddress",ipAddress)