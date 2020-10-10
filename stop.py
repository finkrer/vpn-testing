from imports import CLIENTS, remote_execute

for c in CLIENTS:
    remote_execute(c, 'pkill bash')
