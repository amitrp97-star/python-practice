from netmiko import ConnectHandler

with open ("devices.txt") as file:
 for ip in file:
    ip = ip.strip()

    router = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": "admin",
            "password": "123"
        }
connection = ConnectHandler(**router)
config = connection.send_command ("show runnning-config")

with open (f"backup_{ip}.cfg", "w") as backup:
           backup.write(config)
           connection.disconnect()

           print ("backup succesfully" , ip)

           


           
           




