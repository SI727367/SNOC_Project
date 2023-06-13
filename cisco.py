import paramiko
import telnetlib
import time


def backup(ip_address, username, password, device_name, token):
    try:
        if token == 'telnet':
            tn = telnetlib.Telnet(ip_address)

            tn.read_until(b"Username: ")
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
            tn.write(b"terminal length 0\n")
            tn.write(b"show run\n")
            response = tn.read_all().decode('ascii')

            current_time = time.localtime()
            time_now = time.strftime("%Y-%m-%d-%H-%M-%S", current_time)
            filename = f"{time_now}_{device_name}_config.txt"

            # Write response to file
            with open('backup/cisco/' + filename, 'w') as file:
                file.write(response)

            tn.close()
            file.close()
        else:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip_address, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)

                stdin, stdout, stderr = ssh.exec_command('show run')
                response = stdout.readlines()
                current_time = time.localtime()
                time_now = time.strftime("%Y-%m-%d-%H-%M-%S", current_time)
                filename = f"{time_now}_{device_name}_config.txt"

                # Write response to file
                with open('backup/cisco/' + filename, 'w') as file:
                    for line in response:
                        line = line.strip('\n')
                        file.write(line)

                ssh.close()
                file.close()

            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
