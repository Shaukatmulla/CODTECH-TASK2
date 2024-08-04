import nmap
import requests

def scan_open_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')  # Scan ports 1 to 1024
    open_ports = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    open_ports.append(port)
    return open_ports

def check_software_version(url):
    try:
        response = requests.get(url)
        server = response.headers.get('Server')
        if server:
            return server
        else:
            return "No server version found"
    except requests.RequestException as e:
        return f"Error checking version: {e}"

def main():
    target = input("Enter the target IP or URL: ")
    if target.startswith('http'):
        software_version = check_software_version(target)
        print(f"Software version: {software_version}")
    else:
        open_ports = scan_open_ports(target)
        if open_ports:
            print(f"Open ports: {open_ports}")
        else:
            print("No open ports found")

if __name__ == "__main__":
    main()
