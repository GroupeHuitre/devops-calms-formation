# Module 06 - Infrastructure as Code

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q6.1 à Q6.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q6.1** - Qu'est-ce que l'Infrastructure as Code ?

L'Infrastructure as Code (IaC), c'est décrire son infrastructure (serveurs, réseau, bases de données…) dans des fichiers de code, au lieu de la configurer à la main. Ces fichiers se gèrent comme du code applicatif : ils sont versionnés dans Git, relus en pull request, testés, et peuvent être rejoués autant de fois que nécessaire.

L'intérêt principal, c'est d'avoir des environnements identiques et reproductibles. Martin Fowler explique que la configuration manuelle finit par produire des serveurs « flocons de neige » (*snowflakes*), tous légèrement différents, et qu'on ne sait plus vraiment reconstruire.

Source :

https://martinfowler.com/bliki/InfrastructureAsCode.html

- **Q6.2** - Quelle différence faites-vous entre une approche déclarative et une approche impérative ?

- **Déclarative :** on décrit le résultat voulu (« je veux 3 serveurs avec telle configuration ») et l'outil se débrouille pour y arriver. C'est le cas de Terraform, OpenTofu ou Docker Compose.
- **Impérative :** on décrit les étapes à suivre, dans l'ordre (« crée un serveur, puis installe ceci, puis lance cela »). Un script shell en est l'exemple typique.

La différence se voit surtout quand on relance : un outil déclaratif compare l'existant au résultat voulu et ne fait que ce qui manque, alors qu'un script impératif rejoue toutes ses étapes, ce qui peut créer des doublons ou des erreurs. Ansible est entre les deux : on écrit des tâches dans un ordre précis, mais chaque module décrit un état à atteindre.

Source :

https://developer.hashicorp.com/terraform/intro

- **Q6.3** - Qu'est-ce que l'idempotence ? Qu'avez-vous observé en relançant docker compose up, et en quoi est-ce différent de l'idempotence d'un outil IaC comme Terraform ou OpenTofu ?

Une opération est idempotente si la lancer une fois ou dix fois donne le même résultat. Par exemple, « le fichier doit exister » est idempotent, alors que « ajoute une ligne au fichier » ne l'est pas.

Nous n'avons pas pu lancer `docker compose up` : Docker n'est pas installé sur le poste utilisé (voir section 5). D'après la documentation de Docker, une deuxième exécution ne recrée les conteneurs que si la configuration ou l'image a changé. Sans changement, rien n'est recréé.

La différence avec Terraform ou OpenTofu, c'est l'état. Docker Compose regarde simplement les conteneurs qui tournent sur la machine locale. Terraform, lui, garde un fichier d'état (`terraform.tfstate`) qui lui sert de référence pour comparer la configuration voulue à l'infrastructure réelle, y compris des ressources cloud distantes. Il affiche aussi un plan de ce qu'il va changer avant d'agir, ce que Compose ne fait pas.

Sources :

https://docs.docker.com/reference/cli/docker/compose/up/
https://developer.hashicorp.com/terraform/intro

- **Q6.4** - Docker Compose est-il un outil IaC au même titre que Terraform ou OpenTofu ? En quoi s'inscrit-il malgré tout dans une démarche IaC, et pourquoi ne suffit-il pas à gérer une infrastructure cloud ?

Non. Docker Compose décrit comment lancer une application et ses services sur une machine qui existe déjà. Il ne crée pas de serveurs, de réseaux cloud ou de bases de données managées.

Il s'inscrit quand même dans une démarche IaC : notre `compose.yaml` est un fichier versionné, relu en PR, qui décrit l'environnement de façon déclarative (port, variable d'environnement, contrôle de santé) et qu'on peut rejouer à l'identique sur n'importe quel poste.

Mais il ne suffit pas pour une infrastructure cloud, parce qu'il ne sait pas provisionner de ressources (machines, réseau, DNS, droits d'accès) et qu'il n'a pas de fichier d'état ni de plan à relire avant d'appliquer. Pour ça, il faut un outil comme Terraform ou OpenTofu, qui passe par les API des fournisseurs cloud.

- **Q6.5** - Pourquoi les fichiers d'état (par exemple terraform.tfstate) et les secrets exigent-ils des précautions ?

Le fichier d'état peut contenir des données sensibles en clair, comme des mots de passe de base de données ou des tokens d'API. HashiCorp le dit clairement : il faut le traiter comme une donnée sensible. Même une variable marquée `sensitive` est masquée à l'écran, mais reste stockée dans le state.

Il y a aussi un risque pour l'infrastructure elle-même : un state perdu ou abîmé fait que Terraform ne sait plus ce qu'il gère, et deux personnes qui l'utilisent en même temps peuvent se marcher dessus.

Les bonnes pratiques : ne jamais le committer (notre `.gitignore` exclut bien `*.tfstate` et `*.tfvars`), le stocker à distance avec chiffrement et verrouillage, et limiter qui peut y accéder. Pour les secrets, on les passe par des variables d'environnement ou un coffre-fort à secrets, jamais en dur dans le code.

Source :

https://developer.hashicorp.com/terraform/language/state/sensitive-data

- **Q6.6** - Comparez OpenTofu/Terraform, Ansible et Docker Compose : usage, gestion d'état, idempotence, limites.

| | OpenTofu / Terraform | Ansible | Docker Compose |
|---|---|---|---|
| **Usage** | Créer et gérer des ressources d'infrastructure (cloud, réseau, DNS…) | Configurer des machines existantes (installer, paramétrer, déployer) | Lancer une application multi-conteneurs sur une machine |
| **Gestion d'état** | Fichier d'état qui sert de référence | Pas de fichier d'état : il regarde l'état réel de la machine à chaque exécution | Pas de fichier d'état : il regarde les conteneurs en cours |
| **Idempotence** | Oui, avec un plan à relire avant d'appliquer | Oui pour la plupart des modules, mais pas pour les commandes shell brutes | Oui pour les conteneurs : il ne recrée que ce qui a changé |
| **Limites** | Le state est sensible et doit être protégé | Moins adapté pour créer de l'infrastructure cloud de A à Z | Ne provisionne aucune infrastructure, reste limité à une machine |

OpenTofu est un fork de Terraform, créé après le passage de Terraform sous une licence plus restrictive (BUSL), et confié à la Linux Foundation. Les deux fonctionnent de la même façon.

Sources :

https://opentofu.org/faq/
https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html

- **Q6.7** - Comment intégreriez-vous l'IaC dans un pipeline (plan, revue, application) avec une validation avant la production ?

On traiterait les fichiers IaC comme du code applicatif :

1. **À chaque pull request :** le pipeline vérifie le format et la syntaxe, puis lance un `terraform plan` pour montrer ce qui va changer, sans rien toucher.
2. **Revue :** un collègue relit le code et le plan, surtout les suppressions de ressources.
3. **Après la fusion :** le pipeline refait un plan, l'enregistre dans un fichier, et applique exactement ce plan, d'abord sur un environnement de test.
4. **Avant la production :** une validation humaine obligatoire. HashiCorp conseille de réserver l'application automatique sans validation aux environnements non critiques.

Il faut aussi un state distant avec verrouillage, pour éviter que deux exécutions se lancent en même temps, et des identifiants passés par variables d'environnement.

Source :

https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform

- **Q6.8** - Qu'est-ce que la dérive de configuration, et comment la détecter et la corriger durablement ?

La dérive de configuration, c'est quand l'infrastructure réelle ne correspond plus à ce qui est décrit dans le code. En général, quelqu'un a fait une modification à la main, souvent en urgence pendant un incident, et ne l'a pas reportée dans le code.

**Pour la détecter :** avec Terraform, `terraform plan -refresh-only` compare le state à l'infrastructure réelle et affiche ce qui a changé en dehors de Terraform, sans rien modifier. On peut le lancer régulièrement dans le pipeline, par exemple chaque nuit.

**Pour la corriger :** soit la modification était voulue et on la reporte dans le code, soit elle ne l'était pas et on réapplique le code pour revenir à l'état prévu. Pour que ça dure, le plus important est d'interdire les modifications manuelles en production : tout changement passe par le code et le pipeline.

Source :

https://developer.hashicorp.com/terraform/tutorials/state/refresh

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Déclaratif, impératif, état, idempotence, secrets

- **Déclaratif :** on dit ce qu'on veut obtenir, l'outil trouve comment.
- **Impératif :** on dit quoi faire, étape par étape.
- **État :** la mémoire de l'outil sur ce qu'il gère. Terraform la garde dans un fichier, Ansible et Compose regardent directement la réalité.
- **Idempotence :** relancer ne casse rien et ne crée pas de doublons, on obtient toujours le même résultat.
- **Secrets :** mots de passe, clés, tokens. Ils ne vont jamais dans Git, ni dans le code, ni dans un fichier d'état non protégé.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [Infrastructure As Code](https://martinfowler.com/bliki/InfrastructureAsCode.html) | Martin Fowler | 21/10/2026 | L'IaC consiste à définir l'infrastructure par du code source, géré comme un logiciel (versionnement, tests). La configuration manuelle produit des serveurs « snowflakes » légèrement différents. | Article court, de blog. Ne parle ni d'idempotence ni de dérive de configuration. Publié le 01/03/2016. |
| [What is Terraform?](https://developer.hashicorp.com/terraform/intro) | HashiCorp | 21/10/2026 | Terraform est déclaratif, suit un cycle Write / Plan / Apply, et garde un fichier d'état qui sert de référence sur l'infrastructure réelle. | Documentation officielle de l'éditeur. Pas de date (version 1.16.x). |
| [Manage sensitive data in your configuration](https://developer.hashicorp.com/terraform/language/state/sensitive-data) | HashiCorp | 21/10/2026 | Le state peut contenir des mots de passe et tokens en clair et doit être traité comme une donnée sensible. Recommandations : state distant, chiffrement, accès limité. | Documentation officielle. Pas de date. |
| [Automate Terraform](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform) | HashiCorp | 21/10/2026 | Dans un pipeline : plan enregistré, revue humaine, puis application de ce plan précis. Application automatique à réserver aux environnements non critiques. | Tutoriel officiel. Pas de date. |
| [Detect drift with refresh-only mode](https://developer.hashicorp.com/terraform/tutorials/state/refresh) | HashiCorp | 21/10/2026 | `terraform plan -refresh-only` détecte les changements faits en dehors de Terraform sans rien modifier. Deux corrections possibles : accepter le changement dans le state, ou réappliquer la configuration. | Tutoriel officiel. Pas de date. |
| [docker compose up](https://docs.docker.com/reference/cli/docker/compose/up/) | Docker | 21/10/2026 | Si la configuration ou l'image a changé, `docker compose up` arrête et recrée les conteneurs concernés. `--force-recreate` force la recréation. | La page ne décrit pas explicitement le cas « aucun changement » : on le déduit. Pas de date. |
| [Glossary](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html) | Ansible (Red Hat) | 21/10/2026 | Définition de l'idempotence. Les modules Ansible sont idempotents et ne font de changement que si c'est nécessaire. Pas de démon permanent sur les machines. | Le glossaire ne dit pas explicitement qu'Ansible n'a pas de fichier d'état : c'est notre déduction. Pas de date. |
| [OpenTofu FAQ](https://opentofu.org/faq/) | OpenTofu (LF Projects, Linux Foundation) | 21/10/2026 | OpenTofu est un fork de Terraform, créé après le passage de Terraform sous licence BUSL, et confié à la Linux Foundation. | Page du projet lui-même, donc pas neutre sur la question de la licence. Pas de date. |

## 4. Exemple professionnel commenté

On a repris le cas de Knight Capital, déjà vu au module 1. En août 2012, l'entreprise déploie un nouveau logiciel sur huit serveurs, en copiant le code à la main. Un des huit est oublié et garde l'ancien code. À l'ouverture des marchés, ce serveur réactive une vieille fonction et l'entreprise perd plus de 460 millions de dollars en 45 minutes (sources : SEC et Henrico Dolfing, voir le module 1).

Commentaire : Avec ce module, on voit cette histoire autrement : c'est un cas typique de dérive de configuration. Les huit serveurs étaient censés être identiques, mais l'un d'eux ne l'était plus, et personne ne s'en est rendu compte. Avec une démarche IaC, le même code est appliqué partout et un outil peut comparer l'état réel de chaque serveur à ce qui est prévu. L'oubli aurait été visible avant l'ouverture des marchés.

## 5. Expérimentation / analyse
**Piste :** Fichier Compose versionné (démarche IaC) / comparaison avec les outils IaC OpenTofu/Terraform et avec Ansible

- Hypothèse : Notre `compose.yaml` suffit à décrire et rejouer l'environnement de l'application à l'identique, ce qui en fait un élément d'une démarche IaC, mais il ne permettrait pas de créer une infrastructure de production.

- Protocole / méthode : Docker n'est pas installé sur le poste utilisé (`docker: command not found`). On a donc suivi l'**option B** de la consigne : analyse du `Dockerfile` et du `compose.yaml` sans exécution, puis vérification du `.gitignore`. **Aucune commande Docker n'a été exécutée.**

- Résultat observé ou simulation :

  **Analyse de `application/compose.yaml`**
  - Port : `127.0.0.1:8000:8000`. Le service n'est accessible que depuis la machine elle-même, pas depuis le réseau. C'est un bon choix pour un environnement local.
  - Variable d'environnement : `NOVATECH_HOST: "0.0.0.0"`, pour que l'application écoute dans le conteneur. Aucun secret n'est présent dans le fichier.
  - `build: .` : l'image est construite à partir du `Dockerfile` du même dossier, donc l'environnement est reproductible à partir du dépôt.

  **Analyse de `application/Dockerfile`**
  - Image de base `python:3.12-slim` : version de Python fixée, image légère.
  - Utilisateur non root (`appuser`, uid 10001) : si l'application est compromise, l'attaquant n'a pas les droits root dans le conteneur.
  - `HEALTHCHECK` toutes les 10 s sur `/health` : Docker peut savoir si l'application répond, pas seulement si le conteneur tourne.
  - Point faible : `python:3.12-slim` n'est pas épinglé sur une version précise de l'image. Deux constructions à des dates différentes peuvent donc donner des images légèrement différentes.

  **Vérification du `.gitignore`**
  - Il exclut bien les fichiers d'état (`*.tfstate`, `*.tfstate.*`, `.terraform/`), les variables Terraform (`*.tfvars`), les fichiers `.env` et les clés (`*.pem`, `*.key`).
  - `.env.example` reste autorisé, ce qui permet de documenter les variables attendues sans valeurs réelles.

  **Comparaison** : voir le tableau de la Q6.6.

- Ce que ce résultat ne prouve pas : Comme rien n'a été exécuté, on ne peut pas affirmer que l'application démarre, que le contrôle de santé passe à `healthy`, que l'utilisateur est bien non root à l'exécution, ni que la relance de `docker compose up` ne recrée rien. Ce sont des comportements attendus d'après les fichiers et la documentation. Un `.gitignore` correct n'empêche pas non plus un secret déjà commité par le passé de rester dans l'historique Git. Enfin, aucune ressource cloud n'a été créée, donc la partie Terraform / OpenTofu reste purement théorique.

## 6. Application à NovaTech
- Problème visé : Chez NovaTech, les tests attendent 24 h parce que l'environnement de test n'est pas partagé (`02_Processus_actuel.csv`), et la procédure de retour arrière n'était pas accessible pendant l'incident du 16 octobre.

- Action envisagée : Décrire l'environnement de test dans un fichier Compose versionné, que chaque développeur peut lancer sur son poste en une commande. Dans un second temps, si NovaTech passe sur le cloud, décrire l'infrastructure avec OpenTofu, avec un pipeline plan / revue / application et une validation humaine avant la production.

- Indicateur et risque :

    - Indicateurs : l'attente avant les tests (24 h aujourd'hui), le temps pour qu'un nouveau développeur ait un environnement qui marche, et le nombre de dérives détectées par le pipeline.

    - Risques : l'environnement local peut rester différent de la production, et donner une fausse confiance. Si des modifications manuelles continuent en production, le code ne décrit plus la réalité. Enfin, un state ou un secret mal protégé deviendrait un nouveau risque de sécurité.

## 7. Preuves déposées
**Attendu :** Fichiers As Code, validation (si exécutée), limites
- Liens commits / MR / CI / fichiers :
  - `application/compose.yaml` et `application/Dockerfile` : fichiers As Code analysés ;
  - `.gitignore` : exclusion des fichiers d'état et des secrets ;
  - Validation Docker : **non exécutée** (Docker absent du poste) ;
  - `infrastructure/README.md` : à compléter avec l'analyse de la section 5.

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA nous a permis de mettre au clair notre réflexion, de parfois les simplifier ou les complexifier si elles n'étaient pas assez complètes. Nous avons également utilisé l'IA pour mettre en forme notre travail proprement.

## 10. Questions ouvertes / blocages

- Docker n'est pas installé sur le poste utilisé : si un autre membre l'a, il faudrait refaire l'option A et déposer les vraies sorties des commandes dans `preuves/`.
- Faut-il épingler l'image Python sur une version précise (par exemple par son empreinte) pour que l'environnement soit vraiment reproductible ?
