# Test-Website
### Demo project for hosting testing

### Setup
1. `mkdir programs/Min-REST-API`
1. `nano programs/Min-REST-API/docker-compose.yaml`
1. `sudo nano //etc/systemd/system/min-rest-api.service`
1. `systemctl daemon-reload`
1. `sudo systemctl enable min-rest-api.service`
1. `sudo systemctl start min-rest-api.service`
1. `sudo systemctl status min-rest-api.service`