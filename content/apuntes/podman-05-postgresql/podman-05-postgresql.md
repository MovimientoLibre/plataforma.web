Title: Podman básico: base de datos persistente con PostgreSQL
Slug: podman-05-postgresql
Summary: .
Tags: contenedores
Date: 2020-09-13 20:50
Modified: 2020-09-13 20:50
Category: apuntes
Preview: podman.png
Status: draft


Resumen.

## Por lo pronto

    $ podman pull postgres:12-alpine

    $ podman pull dpage/pgadmin4

PgAdmin necesita que se declaren por lo menos estas dos variables

- `PGADMIN_DEFAULT_EMAIL`: This is the email address used when setting up the initial administrator account to login to pgAdmin. This variable is required and must be set at launch time.
- `PGADMIN_DEFAULT_PASSWORD`: This is the password used when setting up the initial administrator account to login to pgAdmin. This variable is required and must be set at launch time.

O mejor

    $ podman run --rm --name mi_bitacora_pgadmin4 -p 8085:80 -e 'PGADMIN_DEFAULT_EMAIL=guivaloz@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=pa55w0rD' -d dpage/pgadmin4
