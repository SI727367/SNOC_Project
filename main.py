# Project to manage and maintain various networks devices
# External modules
import os
from dotenv import load_dotenv

# Internal modules
import forti
import cisco
import hp

# Load environment variables
load_dotenv()
MY_ENV_VAR = os.getenv('MY_ENV_VAR')

# Define variables from environment variables TEMPORAL
cuser = os.getenv('USER_CISCO')
cpass = os.getenv('PASS_CISCO')
huser = os.getenv('USER_ARUBA')
hpass = os.getenv('PASS_ARUBA')
fw1 = os.getenv('FW1')
fw2 = os.getenv('FW2')
port1 = os.getenv('PORT1')
port2 = os.getenv('PORT2')


# Create folders for backups
os.makedirs('backup', exist_ok=True)
os.makedirs('backup/cisco', exist_ok=True)
os.makedirs('backup/fortigate', exist_ok=True)
os.makedirs('backup/hp', exist_ok=True)


def main():
    # Open CSV file with brand devices, devicename and tokens, ips and tokens
    with open('Calles.csv', 'r') as file:
        # Switchcase to select the brand of the device
        for line in file:
            brand = line.split(';')[0]
            device_name = line.split(';')[1].strip()
            ip = line.split(';')[2]
            token = line.split(';')[3]

            print(f"Backing up {device_name}...")
            if brand == 'CISCO':
                cisco.backup(ip, cuser, cpass, device_name, token)
            elif brand == 'FORTINET':
                forti.backup(ip, token, device_name, fw1, fw2, port1, port2)
            elif brand == 'HPE':
                hp.backup(ip, huser, hpass, device_name)
            else:
                print("Error: Brand not supported")

            print(f"Backup of {device_name} completed\n")


# Run main function
if __name__ == "__main__":
    main()
