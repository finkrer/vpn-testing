#!/usr/bin/env python3

import sys
from imports import remote_execute

CLIENTS_INTERNET = ['157.245.226.39',
                    '157.245.235.228', '157.245.171.85', '64.225.116.23', '64.225.43.30']

SERVERS_INTERNET = ['167.172.202.126', '64.227.50.4',
                    '64.227.54.186', '64.227.54.213', '64.227.62.47']

CLIENTS_WIREGUARD = ['10.90.0.2', '10.90.0.8',
                     '10.90.0.9', '10.90.0.10', '10.90.0.11']

SERVERS_WIREGUARD = ['10.90.0.3', '10.90.0.4',
                     '10.90.0.5', '10.90.0.6', '10.90.0.7']

CLIENTS_OPENVPN = ['10.80.0.2', '10.80.6.2',
                   '10.80.7.2', '10.80.8.2', '10.80.9.2']

SERVERS_OPENVPN = ['10.80.1.2', '10.80.2.2',
                   '10.80.3.2', '10.80.4.2', '10.80.5.2']

vpn = sys.argv[1]

if vpn == 'wireguard':
    CLIENTS = CLIENTS_WIREGUARD
    SERVERS = SERVERS_WIREGUARD
elif vpn == 'openvpn':
    CLIENTS = CLIENTS_OPENVPN
    SERVERS = SERVERS_OPENVPN
else:
    print('Incorrect vpn')
    sys.exit(1)

mode = sys.argv[2]

template = ''
if mode == 'speed':
    template = 'ab -n 5 {0}/1gb.dat &'
elif mode == 'routing':
    template = 'while true; do nmap -p 1-65000 --min-rate 16384 {0}; done'
else:
    print('Incorrect mode')
    sys.exit(1)


for i, c in enumerate(CLIENTS_INTERNET):
    arg = SERVERS[i] if mode == 'speed' else " ".join(SERVERS)
    command = template.format(arg)
    print(command)
    remote_execute(c, command)
