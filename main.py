# Python program to back up various network devices
# External modules
import os
from dotenv import load_dotenv

# Internal modules
import bk_forti

# Load environment variables
load_dotenv()
MY_ENV_VAR = os.getenv('MY_ENV_VAR')

# Define the base URL
furl = os.getenv('BASE_URL')
ftoken = os.getenv('TOKEN')


def main():
    bk_forti.fortigate(furl, ftoken)


# Using the special variable
if __name__ == "__main__":
    main()
