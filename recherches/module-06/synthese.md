# Module 06 - Infrastructure as Code

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q6.1 à Q6.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q6.1** - Qu'est-ce que l'Infrastructure as Code ?

C'est le fait de décrire son infrastructure (serveurs, réseau, bases de données…) dans des fichiers de code, au lieu de la configurer à la main. Ces fichiers sont rangés dans Git comme le reste du code, ce qui permet de les relire, de garder un historique et de recréer le même environnement autant de fois qu'on veut.

Source : https://martinfowler.com/bliki/InfrastructureAsCode.html

- **Q6.2** - Quelle différence faites-vous entre une approche déclarative et une approche impérative ?

Avec l'approche déclarative, on décrit le résultat qu'on veut obtenir, et c'est l'outil qui trouve comment y arriver. Avec l'approche impérative, on décrit les étapes à suivre, une par une, dans l'ordre.

En gros, le déclaratif dit « quoi », l'impératif dit « comment ».

Source : https://developer.hashicorp.com/terraform/intro

- **Q6.3** - Qu'est-ce que l'idempotence ? Qu'avez-vous observé en relançant docker compose up, et en quoi est-ce différent de l'idempotence d'un outil IaC comme Terraform ou OpenTofu ?

Une action est idempotente quand la lancer une fois ou plusieurs fois donne le même résultat. Relancer ne casse rien et ne crée pas de doublons.

On n'a pas pu tester `docker compose up` car Docker n'est pas installé sur notre poste. D'après la documentation, si rien n'a changé, Docker Compose ne recrée pas les conteneurs.

La différence avec Terraform ou OpenTofu, c'est que ces outils gardent un fichier d'état : une sorte de mémoire de tout ce qu'ils gèrent, qui leur permet de comparer ce qui existe à ce qui est prévu. Docker Compose, lui, regarde juste les conteneurs qui tournent sur la machine.

Sources : https://docs.docker.com/reference/cli/docker/compose/up/ et https://developer.hashicorp.com/terraform/intro

- **Q6.4** - Docker Compose est-il un outil IaC au même titre que Terraform ou OpenTofu ? En quoi s'inscrit-il malgré tout dans une démarche IaC, et pourquoi ne suffit-il pas à gérer une infrastructure cloud ?

Non. Docker Compose sert à lancer une application sur une machine qui existe déjà, il ne crée pas d'infrastructure.

Il fait quand même partie d'une démarche IaC, parce que l'environnement de l'application est décrit dans un fichier versionné, qu'on peut relire et rejouer à l'identique.

Mais il ne suffit pas pour le cloud : il ne sait pas créer de serveurs, de réseaux ou de bases de données chez un fournisseur cloud. C'est le rôle d'outils comme Terraform ou OpenTofu.

- **Q6.5** - Pourquoi les fichiers d'état (par exemple terraform.tfstate) et les secrets exigent-ils des précautions ?

Parce qu'ils peuvent contenir des informations sensibles en clair, comme des mots de passe ou des clés d'accès. Si quelqu'un met la main dessus, il peut accéder à l'infrastructure.

Le fichier d'état est aussi important pour l'outil lui-même : s'il est perdu ou abîmé, Terraform ne sait plus ce qu'il gère. Il ne faut donc jamais le mettre dans Git, le stocker dans un endroit sécurisé et limiter qui y a accès. Pareil pour les secrets, qui ne doivent jamais être écrits en dur dans le code.

Source : https://developer.hashicorp.com/terraform/language/state/sensitive-data

- **Q6.6** - Comparez OpenTofu/Terraform, Ansible et Docker Compose : usage, gestion d'état, idempotence, limites.

| | OpenTofu / Terraform | Ansible | Docker Compose |
|---|---|---|---|
| **Usage** | Créer l'infrastructure (serveurs, réseau, cloud) | Configurer des machines qui existent déjà | Lancer une application sur une machine |
| **Gestion d'état** | Fichier d'état | Pas de fichier d'état, il regarde la machine directement | Pas de fichier d'état, il regarde les conteneurs |
| **Idempotence** | Oui | Oui, en grande partie | Oui |
| **Limites** | Le fichier d'état doit être protégé | Moins fait pour créer de l'infrastructure | Ne crée aucune infrastructure |

OpenTofu est une copie libre de Terraform, créée quand Terraform a changé de licence. Les deux fonctionnent pareil.

Sources : https://opentofu.org/faq/ et https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html

- **Q6.7** - Comment intégreriez-vous l'IaC dans un pipeline (plan, revue, application) avec une validation avant la production ?

On traiterait les fichiers d'infrastructure comme du code normal. À chaque modification, le pipeline montre ce qui va changer (le « plan »), sans rien toucher. Un collègue relit les changements. Une fois validés, ils sont appliqués d'abord sur un environnement de test, puis sur la production après une validation humaine.

Source : https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform

- **Q6.8** - Qu'est-ce que la dérive de configuration, et comment la détecter et la corriger durablement ?

C'est quand l'infrastructure réelle ne correspond plus à ce qui est écrit dans le code, en général parce que quelqu'un a fait une modification à la main sans la reporter.

On la détecte en comparant régulièrement le code à la réalité, ce que les outils comme Terraform savent faire. Pour la corriger, soit on reporte la modification dans le code, soit on réapplique le code pour revenir à ce qui était prévu. Et pour que ça ne se reproduise pas, il faut que tous les changements passent par le code, plus jamais à la main.

Source : https://developer.hashicorp.com/terraform/tutorials/state/refresh

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Déclaratif, impératif, état, idempotence, secrets

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [Infrastructure As Code](https://martinfowler.com/bliki/InfrastructureAsCode.html) | Martin Fowler | 21/10/2026 | L'IaC consiste à définir l'infrastructure par du code, géré comme un logiciel (versionnement, tests). | Article de blog court. Publié le 01/03/2016. |
| [What is Terraform?](https://developer.hashicorp.com/terraform/intro) | HashiCorp | 21/10/2026 | Terraform est déclaratif et garde un fichier d'état qui sert de référence sur l'infrastructure réelle. | Documentation officielle de l'éditeur. Pas de date. |
| [Manage sensitive data](https://developer.hashicorp.com/terraform/language/state/sensitive-data) | HashiCorp | 21/10/2026 | Le fichier d'état peut contenir des mots de passe et des clés en clair, et doit être traité comme une donnée sensible. | Documentation officielle. Pas de date. |
| [Automate Terraform](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform) | HashiCorp | 21/10/2026 | Dans un pipeline : plan, revue humaine, puis application du plan validé. | Tutoriel officiel. Pas de date. |
| [Detect drift with refresh-only mode](https://developer.hashicorp.com/terraform/tutorials/state/refresh) | HashiCorp | 21/10/2026 | Terraform peut détecter les changements faits en dehors de lui, puis on corrige soit le code, soit l'infrastructure. | Tutoriel officiel. Pas de date. |
| [docker compose up](https://docs.docker.com/reference/cli/docker/compose/up/) | Docker | 21/10/2026 | Les conteneurs ne sont recréés que si la configuration ou l'image a changé. | Le cas « aucun changement » est déduit, pas écrit tel quel. Pas de date. |
| [Glossary](https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html) | Ansible (Red Hat) | 21/10/2026 | Définition de l'idempotence. Les modules Ansible ne font un changement que si c'est nécessaire. | Le glossaire ne dit pas explicitement qu'Ansible n'a pas de fichier d'état. Pas de date. |
| [OpenTofu FAQ](https://opentofu.org/faq/) | OpenTofu (Linux Foundation) | 21/10/2026 | OpenTofu est un fork de Terraform, créé après son changement de licence. | Page du projet lui-même. Pas de date. |

## 4. Exemple professionnel commenté

## 5. Expérimentation / analyse
**Piste :** Fichier Compose versionné (démarche IaC) / comparaison avec les outils IaC OpenTofu/Terraform et avec Ansible
- Hypothèse :
- Protocole / méthode :
- Résultat observé ou simulation :
- Ce que ce résultat ne prouve pas :

## 6. Application à NovaTech
- Problème visé :
- Action envisagée :
- Indicateur et risque :

## 7. Preuves déposées
**Attendu :** Fichiers As Code, validation (si exécutée), limites
- Liens commits / MR / CI / fichiers :

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a aidé à rédiger les réponses Q6.1 à Q6.8 et a vérifié chaque source (auteur, date, ce que dit réellement la page).

## 10. Questions ouvertes / blocages
