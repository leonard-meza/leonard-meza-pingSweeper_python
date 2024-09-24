import os
import subprocess

def ping_ip(ip):
    command = ['ping', '-n', '3', ip] #"""-n for windows, -c for unix will update w/ logic to distinguish platform and use appropriate flag"""
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = response.stdout.decode()
    print(output)

    if "unreachable" in output.lower():
        return False
    return response.returncode == 0

base_ip = input("Enter the base IP Address (First 3 octets, ex 10.10.10.): ")
start_range = int(input("Enter the starting host number in the last octet (e.g., 192): "))
end_range = int(input("Enter the ending host number for the last octet: "))

for i in range(start_range, end_range + 1):
    my_ip = f"{base_ip}{i}"
    
    if ping_ip(my_ip):
        print(f"\033[1;32mThe Host at {my_ip} is reachable\033[0m")
    else:
        print(f"\033[1;31mThe Host at {my_ip} is unreachable\033[0m")