print("CSN Script for setting up server with nginx!\n")
import paramiko

host = '34.221.201.59'
username = 'ubuntu'
password = ''
key_filename = 'csn-key.pem'

commands = [
    'whoami',
    'sudo apt install nginx -y',
    'curl http://localhost'
]

def ssh_connect(host, username, key_filename, commands):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, key_filename=key_filename)
    
    results ={}
    
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8').strip()
        print(command, ">>>", output)
    
    client.close()

ssh_connect(host, username, key_filename, commands)

