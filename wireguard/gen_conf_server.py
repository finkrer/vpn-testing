import os
import sys

N = 10

SERVER_DATA = """[Interface]
PrivateKey = {0}
Address = 10.90.0.1
ListenPort = 51820

"""

PEER_DATA = """[Peer]
PublicKey = {0}
AllowedIPs = 10.90.0.{1}

"""

if __name__ != "__main__":
    print("I am not a module")
    sys.exit(0)

# gen client configs
os.chdir(os.path.dirname(os.path.realpath(__file__)))
try:
    os.mkdir("server")
except FileExistsError:
    print("Remove ./server dir first")
    sys.exit(1)

with open("server/wg0.conf", "w") as conf:
    server_private_key = open("keys/private0.key").read().strip()
    conf.write(SERVER_DATA.format(server_private_key))

    for i in range(N):
        client_public_key = open(f"keys/public{i+1}.key").read().strip()

        peer_data = PEER_DATA.format(client_public_key, i+2)
        conf.write(peer_data)
print("Finished, check ./server dir")
