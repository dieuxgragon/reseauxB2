from psutil import net_if_addrs

def get_wireless_ip(wireless_interface_name):
    interfaces = net_if_addrs()
    if wireless_interface_name in interfaces:
        for address in interfaces[wireless_interface_name]:
            if address.family == 2:
                return address.address
    return None

wireless_interface_name = 'Wi-Fi'

if __name__ == "__main__":
    ip = get_wireless_ip(wireless_interface_name)
    if ip:
        print(f"{wireless_interface_name}: {ip}")
    else:
        print(f" {wireless_interface_name}.")