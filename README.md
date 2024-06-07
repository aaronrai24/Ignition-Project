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
