#!/usr/bin/env python3

import os
from imports import SERVER, CLIENTS

os.system(
    f'scp ./wireguard/server/wg*.conf ./openvpn/server/*.conf root@{SERVER}:/root/')

server_command_string = f'ssh root@{SERVER} "wg-quick up ~/wg0.conf'
for i, client in enumerate(CLIENTS):
    server_command_string += f'; openvpn --config {i}.conf --daemon'
server_command_string += '"'

os.system(server_command_string)

for i, client in enumerate(CLIENTS):
    os.system(
        f'scp ./wireguard/client/wg{i+1}.conf ./openvpn/client/{i}.conf root@{client}:/root/')
    os.system(
        f'ssh root@{client} "wg-quick up ~/wg{i+1}.conf; openvpn --config {i}.conf --daemon"')
