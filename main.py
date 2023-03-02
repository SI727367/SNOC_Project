# Project to manage and mantain various networks devices
# External modules
import os
from dotenv import load_dotenv

# Internal modules
import forti
import cisco

# Load environment variables
load_dotenv()
MY_ENV_VAR = os.getenv('MY_ENV_VAR')

# Define variables from environment variables TEMPORAL
furl = os.getenv('BASE_URL')
ftoken = os.getenv('TOKEN')
cip = os.getenv('DEVICE_IP')
cuser = os.getenv('USERCISCO')
cpass = os.getenv('PASSWORD')

# Create folders for backups
os.makedirs('backup', exist_ok=True)
os.makedirs('backup/cisco', exist_ok=True)
os.makedirs('backup/fortigate', exist_ok=True)


def main():
    forti.backup(furl, ftoken, "fortigate")
    cisco.backup(cip, cuser, cpass, "cisco")


# Run main function
if __name__ == "__main__":
    main()
