from multiprocessing import connection
import netmiko
import json

devices = '''
192.168.85.131
'''.strip().splitlines()
        
device_type = 'cisco_ios',
username = 'cisco'
password = 'cisco'




for device in devices:
        print('###conneting to to router', device)
        connection = netmiko.ConnectHandler(ip=device, username=username,
                                             password=password, device_type=device_type)
        print(connection.send_command('show clock'))
       
     
