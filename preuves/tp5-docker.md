# TP 5 - Docker Compose (option A, exécution réelle)

**Date :** 21/10/2026
**Poste :** Windows, Docker Desktop 
**Exécuté par :** Morgan

## Étape 1 - Validation du fichier Compose

Commande : `docker compose config`

```
name: application
services:
  novatech-demo:
    environment:
      NOVATECH_HOST: 0.0.0.0
    networks:
      default: null
    build:
      context: C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application
      dockerfile: Dockerfile
    ports:
      - mode: ingress
        host_ip: 127.0.0.1
        target: 8000
        published: "8000"
        protocol: tcp
networks:
  default:
    name: application_default

```

Observation : le fichier est valide et n'affiche aucune erreur, le port ciblé est 8000.

## Étape 2 - Construction et lancement

Commande : `docker compose --build -d`

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose up --build -d
[+] Building 12.4s (12/12) FINISHED
 => [internal] load local bake definitions                                                                         0.1s
 => => reading from stdin 645B                                                                                     0.1s
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 558B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                2.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                      0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/4] FROM docker.io/library/python:3.12-slim@sha256:cb33f7f771ecec2ef1225cf39b159591a040391bd73e4c01f00fdfc4  5.8s
 => => resolve docker.io/library/python:3.12-slim@sha256:cb33f7f771ecec2ef1225cf39b159591a040391bd73e4c01f00fdfc4  0.0s
 => => sha256:5c397e4307db7bd392eff1d36de88b04da2a137a4b906b7e0e4657bada560645 249B / 249B                         0.1s
 => => sha256:b524bb3aba7394d85233f3a0a742b8f1b56179e8f61492f73d42a1ff118623b7 12.12MB / 12.12MB                   1.9s
 => => sha256:be6443c06d3c9914acdca3ffb368adad23d4f282b55e71e730878ad3e3c3f75c 1.29MB / 1.29MB                     0.7s
 => => sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034 29.84MB / 29.84MB                   3.4s
 => => extracting sha256:f2be67225471500c788ce88c597eb5ea8336e912ad1ca4815650e0281afe2034                          1.2s
 => => extracting sha256:be6443c06d3c9914acdca3ffb368adad23d4f282b55e71e730878ad3e3c3f75c                          0.2s
 => => extracting sha256:b524bb3aba7394d85233f3a0a742b8f1b56179e8f61492f73d42a1ff118623b7                          0.7s
 => => extracting sha256:5c397e4307db7bd392eff1d36de88b04da2a137a4b906b7e0e4657bada560645                          0.0s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 1.54kB                                                                                0.0s
 => [2/4] WORKDIR /srv/app                                                                                         0.2s
 => [3/4] COPY app.py ./                                                                                           0.1s
 => [4/4] RUN useradd --create-home --uid 10001 appuser                                                            0.5s
 => exporting to image                                                                                             2.6s
 => => exporting layers                                                                                            0.3s
 => => exporting manifest sha256:fd154f5e22bf484214d9a01061dd4de48f5c19a23ef0c37066eadd6eb28ceb1f                  0.0s
 => => exporting config sha256:433dc7e5f456e0fd38f3d39a1cc31bcc2bae9823a01eeb1bf5f0e6aa2ca1f7a1                    0.0s
 => => exporting attestation manifest sha256:0cb827e3db057f066ee75d053b1482ffdff792204de1f5c26b293e831142270b      0.0s
 => => exporting manifest list sha256:0afc8b240eac6bf130a304995b8cdea882e785040d0f24d4f1f3009fefc93708             0.0s
 => => naming to docker.io/library/application-novatech-demo:latest                                                0.0s
 => => unpacking to docker.io/library/application-novatech-demo:latest                                             2.2s
 => resolving provenance for metadata file                                                                         0.0s
[+] up 3/3
 ✔ Image application-novatech-demo       Built                                                                     18.8s
 ✔ Network application_default           Created                                                                    0.1s
 ✔ Container application-novatech-demo-1 Started

 ```

 Observation : l'image est construite correctement.

 Vérification : `curl.exe http://127.0.0.1:8000/health` 

 ```

 PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> curl.exe http://127.0.0.1:8000/health
{"status": "ok", "service": "novatech-demo"}
PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application>

```

## Étape 3 - Vérification de l'état de santé du conteneur

Commande : `docker compose ps`

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose ps
NAME                          IMAGE                       COMMAND           SERVICE         CREATED         STATUS                   PORTS
application-novatech-demo-1   application-novatech-demo   "python app.py"   novatech-demo   8 minutes ago   Up 8 minutes (healthy)   127.0.0.1:8000->8000/tcp
PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application>

``` 

## Étape 4 - Analyse des logs

Commande : `docker compose logs`

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose logs
novatech-demo-1  | NovaTech demo en écoute sur 0.0.0.0:8000 (santé : /health)
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:03:55] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:06] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:16] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:27] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:37] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:47] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:04:58] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:05:08] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:05:19] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:05:29] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:05:39] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:05:50] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:06:00] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 127.0.0.1 - - [21/Oct/2026 13:06:11] "GET /health HTTP/1.1" 200 -
novatech-demo-1  | 172.18.0.1 - - [21/Oct/2026 13:06:20] "GET /health HTTP/1.1" 200

``` 

Deux origines de requêtes : 127.0.0.1 correspond au HEALTHCHECK exécuté dans le conteneur, 172.18.0.1 à nos requêtes depuis le poste, qui passent par la passerelle du réseau Docker. Cela montre que le conteneur a son propre réseau isolé, relié au poste uniquement par le port 8000.

## Étape 5 - Analyse des logs

Commande : `docker compose exec novatech-demo id`

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose exec novatech-demo id
uid=10001(appuser) gid=10001(appuser) groups=10001(appuser)

```

Observation : l'application tourne avec l'utilisateur appuser (uid 10001), pas root, comme prévu par la ligne USER appuser du Dockerfile. En cas de faille, l'attaquant n'a pas les droits administrateur.

## Étape 6 - Tester l'idempotence

Commande : `docker compose up -d`

Cette fois, sans `--build`, on ne demande pas de construire l'image.

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose up -d
[+] up 1/1
 ✔ Container application-novatech-demo-1 Running

 ```

 Observation : au premier lancement, le conteneur était "Created" puis "Started". À la relance, il est seulement "Running". Docker n'a rien recréé car rien n'a changé. Le "Up" de docker compose ps continue de compter depuis le premier démarrage.

## Étape 7 - Fermer le conteneur

Commande : `docker compose down`

```

PS C:\Users\Morgan\Documents\git\DevOps\devops-calms-formation\application> docker compose down
[+] down 2/2
 ✔ Container application-novatech-demo-1 Removed                                                                    3.4s
 ✔ Network application_default           Removed

 ```

 Et voilà !