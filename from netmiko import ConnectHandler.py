from netmiko import ConnectHandler

Switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.85.135',
    'username': 'cisco',
    'password': 'cisco'
}

net_connect = ConnectHandler(**Switch)
output = net_connect.send_command('show ip int brief')
net_connect.enable()
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,21):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output) 
