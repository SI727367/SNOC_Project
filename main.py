# Project to manage and mantain various networks devices
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
furl = os.getenv('BASE_URL')
ftoken = os.getenv('TOKEN')

cip = os.getenv('CISCO_IP')
cuser = os.getenv('USER_CISCO')
cpass = os.getenv('PASS_CISCO')

hip = os.getenv('ARUBA_IP')
huser = os.getenv('USER_ARUBA')
hpass = os.getenv('PASS_ARUBA')

# Create folders for backups
os.makedirs('backup', exist_ok=True)
os.makedirs('backup/cisco', exist_ok=True)
os.makedirs('backup/fortigate', exist_ok=True)
os.makedirs('backup/hp', exist_ok=True)


def main():
    forti.backup(furl, ftoken, "fortigate")
    cisco.backup(cip, cuser, cpass, "cisco")
    hp.backup(hip, huser, hpass, "aruba")


# Run main function
if __name__ == "__main__":
    main()
