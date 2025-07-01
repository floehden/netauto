import getpass
from netmiko import ConnectHandler

#password = getpass.getpass("Enter password: ")
ips = ["172.20.20.2","172.20.20.3"] 
router = {
    'host': "",
    'port': '22',
    'username': "admin",
    'password': "admin",
    'device_type': 'arista_eos',
    'secret': "admin",
    'verbose': True
}

for i in range(len(ips)):
    router['host'] = ips[i]
    print(f"Connecting to {router['host']}")

    connection = ConnectHandler(**router)
    prompt=connection.find_prompt()
    if '>' in prompt:
        print('Entering enable mode')
        connection.enable()

    print('Sending commands from file')
    output = connection.send_config_from_file(f'router{i+1}.txt')
    print(output)

    connection.send_command('write memory')

    if connection.check_config_mode():
        connection.exit_config_mode()

    print(f"Close connection to {router['host']}")
    connection.disconnect()

    print('#' * 50)