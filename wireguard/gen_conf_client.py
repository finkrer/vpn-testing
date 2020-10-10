import os
import sys

N = 10

CLIENT_DATA = """[Interface]
PrivateKey = {0}
Address = 10.90.0.{1}

"""

PEER_DATA = """[Peer]
PublicKey = {0}
Endpoint = 167.71.157.250:51820
AllowedIPs = 10.90.0.0/24
PersistentKeepalive = 25

"""

if __name__ != "__main__":
    print("I am not a module")
    sys.exit(0)

# gen client configs
os.chdir(os.path.dirname(os.path.realpath(__file__)))
try:
    os.mkdir("client")
except FileExistsError:
    print("Remove ./client dir first")
    sys.exit(1)

server_public_key = open("keys/public0.key").read().strip()

for i in range(N):
    client_private_key = open(f"keys/private{i+1}.key").read().strip()

    data = CLIENT_DATA.format(client_private_key, i+2)
    with open(f"client/wg{i+1}.conf", "w") as conf:
        conf.write(data)
        conf.write(PEER_DATA.format(server_public_key))

print("Finished, check ./client dir")
