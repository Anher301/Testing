from importlib.resources import read_text
from os import read
import yaml
from pprint import pprint
from netmiko import ConnectHandler

def read_yaml(yaml_file):
	with open(yaml_file) as f:
			inventory = f.read()

	inventory_dict = yaml.full_load(inventory)
	return inventory_dict

def device_connection(router_ip):
	device = {
		'device_type' : 'cisco_ios',
		'ip' : '192.168.85.140',
	    'username': 'cisco',
		'password': 'cisco'
}

	conn = ConnectHandler(**device)
	conn.enable()
	conn.find_prompt()
	return conn 
	       

def conf_dhcp(conn, dhcp_config):
	pool = dhcp_config['pool']
	network = dhcp_config['network']
	gateway = dhcp_config['gateway']
	config_list = ['ip dhcp pool {}'.format(pool), 
				'network {}'.format(network),
				'default-router {}'.format(gateway)]
	print (conn.send_config_set(config_list))



def main():
		yaml_file = 'inventory.yaml'
		inventory_dict = read_yaml(yaml_file)
		print(inventory_dict)

		for router in inventory_dict['CORE']:

			router_ip = router['host']
			print ("-------------------------------")
			print ("Configuring{}".format (router_ip))
			print ("-------------------------------")
			#connection
			conn = device_connection(router_ip)


			dhcp_config = router['dhcp_config']
			for config in dhcp_config:
				conf_dhcp(conn, config)

                
main()


'''Device = {
	      'device_type': 'cisco_ios',
          'ip': '192.168.85.129',
          'username': 'cisco',
		  'password': 'cisco',
		  'secret': 'cisco'
		 
}


net_connect = ConnectHandler(**Device)
net_connect.enable()
net_connect.find_prompt()
net_connect.config_mode()
dhcp_config = ['ip dhcp pool 1', 'network 192.168.85.0 255.255.255.0', 'domain-name cisco.com', 'dns server 8.8.8.8', 'default-router 192.168.85.2 255.255.255.0', 'ip dhcp excluded-address 192.168.85.1 192.168.85.25']
net_connect.find_prompt()
dhcp = net_connect.send_config_set(dhcp_config)
print('dhcp')'''












