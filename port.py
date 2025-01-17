import socket

def main():
    target_host = input("Enter the target host (e.g., example.com): ")
    port_range = range(1, 1000)

    for port in port_range:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print("Port {} is open".format(port))
            sock.close()
        except socket.error:
            pass

if __name__ == "__main__":
    main()
