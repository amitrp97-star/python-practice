
from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",
    "username": "admin",
    "password": "Cisco123"
}

connection = ConnectHandler(**router)

config = connection.send_command("show running-config")

with open("router_backup.cfg", "w") as file:
    file.write(config)

connection.disconnect()

print("Router backup completed")