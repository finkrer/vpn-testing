#!/usr/bin/env python3

from imports import SERVER, CLIENTS, remote_execute

remote_execute(SERVER, 'wg-quick down ~/wg0.conf; pkill openvpn; rm *.conf')
for i, client in enumerate(CLIENTS):
    remote_execute(
        client, 'wg-quick down ~/wg{i+1}.conf; pkill openvpn; rm *.conf')
