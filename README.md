# Test-Website
### The project for hostings and Docker containers testing

### Server setup
1. `mkdir programs/Min-REST-API`
1. `nano programs/Min-REST-API/docker-compose.yaml`
1. `sudo nano //etc/systemd/system/min-rest-api.service`
1. `systemctl daemon-reload`
1. `sudo systemctl enable min-rest-api.service`
1. `sudo systemctl start min-rest-api.service`
1. `sudo systemctl status min-rest-api.service`

### Dev setup
1. Optional PowerShell permitions: `Set-ExecutionPolicy unrestricted`
1. `python -m venv venv`
1. `.\venv\Scripts\activate`
1. `pip install -r .\requirements.txt`
1. `flask --app run_server.py --debug run --host=0.0.0.0 --port=5005`
