# Igniton Backup Review Projects

This repository servers as a template for reviewing Ignition backups. The backups are stored in the `backups` directory, and if configured in the compose file will automatically restore when the container is initially created.

## Projects included

- APC
- SC-Production
- Harlan

___

## Prerequisite

Understand the process of creating docker containers using the [docker-image](https://github.com/design-group/ignition-docker).

This project assumes you have a local DG Traefik reverse proxy running, if not, the script will set one up or you can set one up using this repository [dg-traefik-proxy](https://github.com/design-group/dg-traefik-proxy)

All Design Group project repositories use the following automation tools:

- [pre-commit](https://pre-commit.com/)
- [pylint](https://pylint.org/)
- [markdownlint](https://github.com/markdownlint/markdownlint)
- [shellcheck](https://github.com/koalaman/shellcheck)
- [yamllint](https://github.com/adrienverge/yamllint)

Please confirm they are present in your environment before continuing.

### Adding a new Gateway

To add a new gateway, create a new branch off of `master` and name it the gateway name. For example, if you are adding a new gateway for `Harlan`, create a branch named `harlan`. Start up the containers and navigate to the gateway's web interface. Go to `Config` -> `Restore/Backup` -> `Restore` and upload the backup file. Once the backup is restored, run the `download-gateway-backups.sh` script to download the backup. Commit the backup to the `backups` directory and push the branch to the repository. 

You will need to reset the gateway password most likely. You can do this by running the following command:

```bash
docker exec <container name> bash -c "./gwcmd.sh -p && ./gwcmd.sh -r"
```
