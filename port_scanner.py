import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Short timeout for faster scan
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    if not open_ports:
        print("No open ports found in the given range.")
    return open_ports

def main():
    ip = input("Enter IP address to scan: ").strip()
    if not is_valid_ip(ip):
        print("Invalid IP address.")
        return

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("Invalid port range. Ports must be between 1 and 65535 and start <= end.")
        return

    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()
