# Drone CI – Setup

## Startup
### Startup – Drone CI
```sh
docker-compose -f docker-compose.yml -f docker-compose.dropbox.yml up -d

```

### Startup – serveo.net
```sh
while true; do ssh -i ./data/serveo.net/id_rsa -R ci.signalwerk.ch:80:localhost:80 serveo.net; done
```




## Setup
* clone
* copy configs & edit
```sh
cp ./data/config/.dropbox_uploader_default ./data/config/.dropbox_uploader
cp ./.env_default ./.env
```
* startup (see Startup-Section)


## Rebuild Dropbox Uploader

```sh
docker-compose stop
docker-compose -f docker-compose.dropbox.yml build --no-cache
```

Uploader can be found [here](https://github.com/andreafabrizi/Dropbox-Uploader).


### Todo
#### Restart if not available
* [web check](https://serverfault.com/questions/562524/bash-script-to-check-if-a-public-https-site-is-up)
* [Restart Process](https://www.oipapio.com/question-238641)
