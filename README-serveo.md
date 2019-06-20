## DNS setup for serveo
See also [serveo.net](https://serveo.net/)

### Key
Generat a new key and with ssh:
```
ssh-keygen -t rsa -b 4096 -C "sh@signalwerk.ch"
```

### Fingerprint
Get a Fingerprint of the new key:
```
ssh-keygen -l -f ./data/serveo.net/id_rsa
```

### DNS-Records
Add two new records for ci.signalwerk.ch
```
CNAME: 159.89.214.31.
TXT: authkeyfp=SHA256:0000000000000000000000000000000000000000000
```

### Start via SSH
```
ssh -i ./data/serveo.net/id_rsa -R ci.signalwerk.ch:80:localhost:80 serveo.net
```
or run it endless in case it stops connection
```
while true; do ssh -i ./data/serveo.net/id_rsa -R ci.signalwerk.ch:80:localhost:80 serveo.net; done
```
