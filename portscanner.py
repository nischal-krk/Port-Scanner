import socket
import pyfiglet
import sys
from datetime import datetime

banner = pyfiglet.figlet_format("SCANNER BY NIK")
print(banner)

if len(sys.argv) == 2:
    target_ip = socket.gethostbyname(sys.argv[1])

else:
    print("Bad argument. Enter again.")

print("-"*100)
print("IP address to scan: ", target_ip)
print("Scanning started at: ",datetime.now())
print("-"*100)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(1,101):

        res = s.connect_ex((target_ip,port))

        if res == 0:
            print("         ")
            print("Open port: ", port)
            print("         ")
        
        else :
            print("Closed port: ", port)

    s.close()

except KeyboardInterrupt:
    print("         ")
    print("Keyboard interrupt detected.....Exiting now......")
    print("         ")

except socket.error:
    print("         ")
    print("Socket error detected.....Exiting now......")
    print("         ")

except socket.gaierror:
    print("         ")
    print("Socket error detected.....Exiting now......")
    print("         ")