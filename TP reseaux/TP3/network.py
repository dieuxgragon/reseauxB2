from psutil import net_if_addrs
import os
import sys
from socket import gethostbyname
from sys import argv

def lookup(name):
        name = input("rentrer le host name ")
        ipAddress = gethostbyname(name)
        print("ipAddress",ipAddress)

def ping(ip):
     os.system(f"ping {argv[1]}")

def get_ip():
    try:
        wireless_interface_name = 'Wi-Fi'
        ip = get_wireless_ip(wireless_interface_name)
        if ip:
            print(ip)
        else:
            print(f"No IPv4 address found for interface {wireless_interface_name}.")
    except Exception as e:
        print(e)

def get_wireless_ip(wireless_interface_name):
    for interface in net_if_addrs():
        if interface == wireless_interface_name:
            for address in net_if_addrs()[interface]:
                if address.family == 2:
                    return address.address
    return None

if len(sys.argv) < 2:
    print("Usage: python network.py <command> [argument]")
else:
    command = sys.argv[1]

    if command == "lookup":
        if len(sys.argv) < 3:
            print("Usage: python network.py lookup <hostname>")
        else:
            lookup_host(sys.argv[2])
    elif command == "ping":
        if len(sys.argv) < 3:
            print("Usage: python network.py ping <ip_address>")
        else:
            ping_host(sys.argv[2])
    elif command == "ip":
        get_ip()
    else:
        print(f"'{command}' is not an available command. Déso.")

