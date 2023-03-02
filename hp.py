import paramiko
import time


def backup(ip_address, username, password, device_name):
    try:
        # Try to establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_address, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)

        stdin, stdout, stderr = ssh.exec_command('display current-configuration')
        response = stdout.readlines()

        current_time = time.localtime()
        time_now = time.strftime("%Y-%m-%d-%H-%M-%S", current_time)
        filename = f"{time_now}_{device_name}_config.txt"

        # Write response to file
        with open('backup/hp/' + filename, 'w') as file:
            for line in response:
                if line.strip():  # checks if the line is not empty or whitespace only
                    file.write(line.strip() + '\n')  # writes the line without leading/trailing whitespace

        ssh.close()
        file.close()

    # If SSH connection fails, return an error message
    except paramiko.ssh_exception.SSHException:
        return "Error: SSH connection failed"
