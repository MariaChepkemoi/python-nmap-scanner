 
import nmap

# Initialize the scanner
scanner = nmap.PortScanner()

print("Welcome to the Nmap Scanner!")
target = input("Enter the IP address or domain to scan: ")
scanner.scan(target, '1-1024')  # Scan ports 1 to 1024

print(f"\nScanning results for: {target}")
for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():
        print(f"\nProtocol: {proto}")

        ports = scanner[host][proto].keys()
        for port in sorted(ports):
            print(f"Port: {port}\tState: {scanner[host][proto][port]['state']}")

