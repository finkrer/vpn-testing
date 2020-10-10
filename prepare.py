from imports import remote_execute

new_machines = ['64.227.50.4', '64.227.54.186', '64.227.54.213', '64.227.62.47',
                '157.245.235.228', '157.245.171.85', '64.225.116.23', '64.225.43.30']
servers = new_machines[:4]
clients = new_machines[4:]

common_tasks = 'apt update; apt install openvpn wireguard prometheus-node-exporter'

for c in clients:
    remote_execute(c, 'apt install nmap')

# for c in clients:
#     os.system(
#         f'ssh root@{c} "{common_tasks} apache2-utils"')

# for s in servers:
#     os.system(
#         f'ssh root@{s} "{common_tasks} nginx; dd if=/dev/urandom of=/var/www/html/1gb.dat bs=512 count=2M; dd if=/dev/urandom of=/var/www/html/1.dat bs=1 count=1"')
