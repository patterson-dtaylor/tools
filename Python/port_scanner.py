import sys
import socket
from datetime import datetime
from unittest import result

common_ports = [21, 22, 25, 53, 80, 123, 179, 443, 500, 3389]

#Define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid ammount of args.")
    print("Syntax: python3 port_scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        print(f"Checking port: {port}")
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit