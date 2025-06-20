import time
import paramiko

# preparing data
router1 = {
    'hostname': '172.20.20.2',
    'port': '22',
    'username': 'admin',
    'password': 'admin',
}

router2 = {
    'hostname': '172.20.20.3',
    'port': 22,
    'username': 'admin',
    'password': 'admin',
}

commands1 = [
    "enable",
    "configure",
    "ip routing",
    "interface Ethernet1",
    "no switchport",
    "ip address 192.168.1.1/24",
    "exit",
    "interface Loopback0",
    "ip address 10.10.10.1/32",
    "exit",
    "router bgp 65001",
    "router-id 10.10.10.1",
    f"neighbor 192.168.1.2 remote-as 65001",
    "network 10.10.10.1/32",
    "exit",
    "exit",
]

commands2 = [
    "enable",
    "configure",
    "ip routing",
    "interface Ethernet1",
    "no switchport",
    "ip address",
    "ip address 192.168.1.2/24",
    "exit",
    "interface Loopback0",
    "ip address 10.10.10.2/32",
    "exit",
    "router bgp 65001",
    "router-id 10.10.10.2",
    "neighbor 192.168.1.1 remote-as 65001",
    "network 10.10.10.2/32",
    "exit",
    "exit",
]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connecting to the router
print("Connecting to Router 1...")
ssh_client.connect(**router1,look_for_keys=False, allow_agent=False)
shell1 = ssh_client.invoke_shell()

print("Router 1 connected. Configuring...")
for command in commands1:
    shell1.send(command + "\n")
    time.sleep(0.5)  # wait for the command to be processed
print("Router 1 configuration complete.")
ssh_client.close()
print("Connection to Router 1 closed.")

# connecting to the second router
print("Connecting to Router 2...")
ssh_client.connect(**router2,look_for_keys=False, allow_agent=False)
shell2 = ssh_client.invoke_shell()
print("Router 2 connected. Configuring...")
for command in commands2:
    shell2.send(command + "\n")
    time.sleep(1)  # wait for the command to be processed
print("Router 2 configuration complete.")
# closing the connections
ssh_client.close()
print("Connection to Router 2 closed.")



