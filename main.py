# Project to manage and maintain various networks devices
# External modules
import os

# Internal modules
import forti
import cisco
import hp

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
                cisco.backup(ip, device_name, token)
            elif brand == 'FORTINET':
                forti.backup(ip, token, device_name)
            elif brand == 'HPE':
                hp.backup(ip, device_name)
            else:
                print("Error: Brand not supported")

            print(f"Backup of {device_name} completed\n")


# Run main function
if __name__ == "__main__":
    main()
