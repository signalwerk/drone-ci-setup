# Startup

```sh

docker-compose -f docker-compose.yml -f docker-compose.dropbox.yml up -d
while true; do ssh -i ./data/serveo.net/id_rsa -R ci.signalwerk.ch:80:localhost:80 serveo.net; done

```

## Rebuild Dropbox Uploader

```sh
docker-compose stop
docker-compose -f docker-compose.yml -f docker-compose.dropbox.yml build --no-cache
```

Uploader can be found [here](https://github.com/andreafabrizi/Dropbox-Uploader).
