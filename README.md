# TruStarChallenge
A challenge for a TruSTAR Python developer position

## Requisites
### Usage
* Docker (https://docs.docker.com/engine/install/)
* Docker-Compose (https://docs.docker.com/compose/install/)
### Development
* Python 3.8 (https://www.python.org/downloads/)
* Make (https://www.gnu.org/software/make/)
* Pipenv (https://pypi.org/project/pipenv/)

## Usage
### Set Up
* Edit .env file
* Configure host and port ( defaults: 'localhost' and 4000)
* Start server `docker-compose up -d`
### Get Malware records from Mitre repository
* Use any API runner ( Postman, fetch api, etc )
* POST to http://localhost:4000/mitre ( replace host and port as needed ) with JSON body:
  * path: Folder path from https://github.com/mitre/cti
  * keys: An array with all the wanted keys from the JSON files found in path
### Example
* Method: POST
* Endpoint: http://localhost:4000/mitre
* Request Body: `{
    "path": "/enterprise-attack/attack-pattern",
    "keys": ["id", "objects[0].name", "objects[0].kill_chain_phases"]
}`
* Response Body: `{"data": [{"id": "bundle--c321e442-bbf7-4448-b266-7e9b35e291b9", "objects[0].name": "Extra Window Memory Injection",
"objects[0].kill_chain_phases": [{"kill_chain_name": "mitre-attack", "phase_name": "defense-evasion"},
{"kill_chain_name": "mitre-attack", "phase_name": "privilege-escalation"}]}, {"id":
"bundle--d65aa246-3272-4253-8252-6b6e50906c49", "objects[0].name": "Indicator Removal from Tools"}, {"id":
"bundle--8ecdd49f-9179-43f7-ab45-d1a4082a6b52", "objects[0].name": "System Owner/User Discovery",
"objects[0].kill_chain_phases": [{"kill_chain_name": "mitre-attack", "phase_name": "discovery"}]}, ......,  {"id":
"bundle--82ba5532-29b6-4568-8461-204cc0f99e09", "objects[0].name": "Windows Admin Shares"}, {"id":
"bundle--aaf675ae-c98d-4341-816f-9a8d54299b67", "objects[0].name": "SQL Stored Procedures",
"objects[0].kill_chain_phases": [{"kill_chain_name": "mitre-attack", "phase_name": "persistence"}]}]}`

## Development
* Start development server `make dev`
* Run types checker `make types`
* Run tests `make test`
* Run linter `make lint`
