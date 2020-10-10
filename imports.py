import shlex
import subprocess

SERVER = '167.71.157.250'

CLIENTS = ['157.245.226.39', '167.172.202.126', '64.227.50.4', '64.227.54.186', '64.227.54.213', '64.227.62.47',
           '157.245.235.228', '157.245.171.85', '64.225.116.23', '64.225.43.30']


def remote_execute(host, command):
    command = f'ssh root@{host} "{command}"'
    args = shlex.split(command)
    subprocess.Popen(args, stdout=subprocess.DEVNULL)
