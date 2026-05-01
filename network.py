import socket
import platform
import psutil

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def get_system_info():
    return platform.platform()

def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    result = {}

    for iface, addrs in interfaces.items():
        ips = []
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ips.append(addr.address)
        if ips:
            result[iface] = ips

    return result


if __name__ == "__main__":
    print("=== Python 第一个网络工具 ===\n")

    print("主机名:", get_hostname())
    print("本地IP:", get_local_ip())
    print("系统信息:", get_system_info())

    print("\n网卡信息:")
    for iface, ips in get_network_interfaces().items():
        print(f"  {iface}: {ips}")