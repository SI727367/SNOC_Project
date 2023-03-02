import time
import requests
import urllib3


def backup(baseurl, token, device_name):
    # Disable insecure request warnings
    urllib3.disable_warnings()

    # Create a new HTTP session
    session = requests.Session()

    # Allow connections to servers with untrusted certificates
    session.verify = False

    # Define the API endpoint for backup
    backup_url = ''.join([baseurl, 'monitor/system/config/backup'])

    # Define the API endpoint for backup status
    # Add token to URL query parameter
    endpoint = ''.join([backup_url + "?access_token=" + token + "&scope=global"])

    # Define the request parameters
    request_body = {
        "scope": "global"
    }

    # Create a new HTTP request
    headers = {
        "Content-Type": "application/json",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }

    # Send the request
    response = session.get(endpoint, headers=headers, json=request_body)

    # Read the response body
    response_data = response.content

    current_time = time.localtime()
    time_now = time.strftime("%Y-%m-%d-%H-%M-%S", current_time)
    filename = f"{time_now}_{device_name}_config.txt"

    # Write response to file
    with open('backup/fortigate/' + filename, 'wb') as file:
        file.write(response_data)


