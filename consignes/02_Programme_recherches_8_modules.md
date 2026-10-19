# Programme de formation DevOps

**Approche pédagogique :** recherche collaborative avec ou sans assistant IA, l'expérimentation pratique et l'application des connaissances à une problématique d'entreprise.

## Objectif général de la formation

Comprendre les principes fondamentaux de DevOps dans ses dimensions organisationnelle, culturelle et technique, découvrir les pratiques qui favorisent la collaboration et la livraison continue, et apprendre à construire une démarche d'adoption DevOps adaptée aux besoins d'une entreprise.

## Comment utiliser ce programme pour vos recherches

Pour chaque module, vous trouverez : les **notions** à couvrir, puis un **guide de recherche** avec des questions pour vous aider dans les recherches et des **consignes d'expérimentation**. Les données citées sont dans `donnees-novatech/` ; le détail technique des TP est dans `consignes/06_TP_et_experimentations.md`.

**Règles de réponse :**

- Répondre dans `recherches/module-XX/synthese.md`, en indiquant le numéro de la question (par exemple « Q1.3 »).
- Citer au moins une source vérifiable par réponse (lien, auteur ou éditeur, date de consultation). Une réponse d'assistant IA n'est pas une source.
- Distinguer **faits** (données du dossier, résultats observés), **hypothèses** et **informations à demander**.
- Chaque membre doit pouvoir expliquer oralement, sans IA, au moins une réponse par niveau traité.
- Ne jamais présenter comme réalisée une expérimentation qui n'a pas eu lieu : écrire « non testé » ou « simulé ».

---

## Jour 1 - Comprendre DevOps : origines, principes et écosystème

**Objectif de la journée :** comprendre pourquoi DevOps est apparu, les enjeux auxquels il répond, les principes qui le structurent et ses relations avec les autres approches de gestion et de développement informatique.

### Module 1 - Introduction et exploration de DevOps

#### 1.1. Découvrir DevOps

- Définition et objectifs de DevOps.
- Origine de l'appellation et émergence du mouvement DevOps.
- Contexte historique et évolution des pratiques informatiques.
- Évolution de DevOps et de son adoption dans les organisations.
- Comprendre ce qu'est DevOps et ce qu'il n'est pas.
- Identifier les principaux enjeux du développement et de l'exploitation des applications.

#### 1.2. Comprendre l'importance de DevOps pour l'entreprise

**Perspective Business**

**Perspective IT**

#### 1.3. Comprendre les difficultés des organisations traditionnelles

> **Recherche et expérimentation :** analyser les conflits entre les équipes Dev et Ops de NovaTech et identifier leurs conséquences techniques, organisationnelles et métier.

#### Guide de recherche — Module 1

**Questions de recherche**

- **Q1.1** - Comment définiriez-vous DevOps en une phrase, sans citer aucun outil ?
- **Q1.2** - D'où vient le terme « DevOps » et quels événements des années 2008-2009 ont marqué l'émergence du mouvement ?

- **Q1.3** - D'après les témoignages de `01_Contexte_et_temoignages.md`, quels objectifs des équipes Dev, Ops, sécurité et métier de NovaTech sont contradictoires ?
- **Q1.4** - Pourquoi DevOps n'est-il ni un intitulé de poste, ni une équipe dédiée, ni une chaîne d'outils ? Donnez un exemple d'entreprise où cette confusion a posé problème.

- **Q1.5** - Quelles conséquences métier (clients, chiffre d'affaires, image) l'incident du 16 octobre peut-il avoir, et quelles informations manquent pour les évaluer ?
- **Q1.6** - Parmi les causes possibles des difficultés de NovaTech, lesquelles relèvent des outils, des processus ou de la collaboration ? Sur quels faits du dossier vous appuyez-vous ?

- **Q1.7** - Le stéréotype « Dev veut changer, Ops veut stabiliser » est-il encore pertinent avec le cloud, le SRE et le Platform Engineering ? Argumentez avec au moins deux sources.
- **Q1.8** - Comment démontreriez-vous à la direction de NovaTech la valeur d'une démarche DevOps sans inventer de retour sur investissement ?

**Consignes d'expérimentation**

- **Objectif :** comprendre les conflits Dev/Ops/métier/sécurité et leurs effets, en séparant faits et hypothèses (TP 1).
- **Matériel et données :** `donnees-novatech/01_Contexte_et_temoignages.md` et `03_Incident_fictif.md`.

**Étapes :**

1. Répartir les rôles : métier, développement, exploitation (la sécurité est jouée à tour de rôle).
2. Rejouer en 10 minutes la réunion qui suit l'incident du vendredi 16 octobre, chacun défendant les objectifs de son rôle.
3. Faire tourner les rôles et rejouer une fois.
4. Lister ensemble les frictions observées et les passages de relais problématiques.
5. Remplir le tableau de diagnostic : symptôme / hypothèse de cause / preuve nécessaire / effet métier.
6. Proposer deux façons de faire participer toutes les fonctions dès la conception.

- **Critère de réussite :** au moins trois causes possibles, chacune avec la pièce manquante qui permettrait de la vérifier, et deux propositions reliant coopération et valeur métier.
- **Trace dans le dépôt :** `novatech/diagnostic.md` et `recherches/module-01/synthese.md`.
- **Limites à documenter :** jeu de rôles fondé sur des témoignages fictifs ; aucune cause n'est prouvée sans les pièces manquantes de l'incident.

### Module 2 — Principes fondamentaux et pratiques essentielles DevOps

#### 2.1. Comprendre le framework DevOps Three Ways de Gene Kim

#### 2.2. Découvrir les méthodes d'amélioration des processus

- Introduction à la théorie des contraintes (Theory of Constraints).
- Identification et analyse des goulots d'étranglement.
- Introduction à la cartographie des flux de valeur (Value Stream Mapping).
- Identification des activités créatrices et non créatrices de valeur.
- Découverte de Kanban : principes et visualisation des activités.
- Comprendre le cycle PDCA
- Introduction à l'Improvement Kata.

#### 2.3. Identifier les principales pratiques DevOps

- Comprendre la notion de chaîne de livraison continue.
- Introduction à l'intégration continue (CI).
- Livraison continue et déploiement continu (CD).
- Automatisation des tests et contrôles qualité.
- Gestion des configurations et des environnements.
- Introduction à l'observabilité et à la supervision.
- Découverte de DevSecOps
- Découverte de ChatOps 
- Identifier les mécanismes de feedback dans le cycle de livraison.
- Évaluer la fiabilité d'un processus de livraison.

> **Recherche et expérimentation :** cartographier le processus de livraison de NovaTech, identifier les étapes problématiques et proposer des améliorations à partir des Three Ways, de Kanban et de la théorie des contraintes.

#### Guide de recherche — Module 2

**Questions de recherche**

- **Q2.1** - Quelles sont les trois voies de Gene Kim ? Expliquez chacune en une phrase avec un exemple.
- **Q2.2** - Qu'est-ce qu'un goulot d'étranglement, et qu'est-ce qu'une limite de travail en cours (WIP) ?

- **Q2.3** - À partir de `02_Processus_actuel.csv`, calculez le temps actif, l'attente, le délai total et la part d'attente. Que révèlent ces chiffres ?
- **Q2.4** - Quelle différence faites-vous entre intégration continue, livraison continue et déploiement continu ?

- **Q2.5** - La plus longue attente du processus est-elle forcément la contrainte du système ? Quelles données manquent pour le démontrer ?
- **Q2.6** - Pourquoi limiter le travail en cours peut-il réduire le délai de livraison alors que l'équipe démarre moins de tâches ? Appuyez-vous sur la loi de Little.

- **Q2.7** - Concevez une expérience PDCA ou Improvement Kata pour réduire l'attente avant validation : hypothèse, changement limité, mesure, critère d'arrêt.
- **Q2.8** - Comment les trois voies se renforcent-elles ? Donnez un exemple où améliorer le Flow sans Feedback aggrave la situation.

**Consignes d'expérimentation**

- **Objectif :** cartographier le flux de livraison de NovaTech, repérer les attentes et démarrer un tableau Kanban (TP 2).
- **Matériel et données :** `donnees-novatech/02_Processus_actuel.csv`, tableau Kanban de la plateforme (GitHub Projects ou GitLab Issue Boards).

**Étapes :**

1. Représenter les étapes dans l'ordre : spécification → développement → revue → tests → validation → déploiement.
2. Pour chaque étape, noter le temps actif et l'attente ; calculer les totaux et la part d'attente.
3. Identifier la plus longue attente, sans la déclarer « contrainte » sans données de capacité ni de débit.
4. Proposer une mesure de feedback plus précoce et un essai d'amélioration limité et mesurable.
5. Classer chaque action proposée dans Flow, Feedback ou Continual Learning & Experimentation.
6. Créer le tableau Kanban de l'équipe (À faire, En cours, En revue, Terminé), une carte par livrable, avec une définition de « Terminé » et une limite WIP si utile.

- **Critère de réussite :** calculs justes et unités indiquées, distinction observation / hypothèse, expérience d'amélioration falsifiable, tableau Kanban utilisé.
- **Trace dans le dépôt :** `novatech/value-stream-map.md`, une Issue d'expérimentation, lien ou capture du tableau Kanban, `recherches/module-02/synthese.md`.
- **Limites à documenter :** VSM simplifiée : pas de parallélisme, de variabilité ni de capacité des équipes ; données fictives.

### Module 3 - DevOps et les autres approches de l'IT

#### 3.1. DevOps et Agile

- Rappel des principes fondamentaux du Manifeste Agile.
- Comprendre la complémentarité entre Agile et DevOps.
- Place de DevOps dans une organisation utilisant Scrum ou Kanban.

#### 3.2. DevOps et Lean

- Origines et principes fondamentaux du Lean.
- Application du Lean aux processus informatiques.

#### 3.3. DevOps et la gestion des services informatiques (ITSM)

- Introduction à l'IT Service Management (ITSM).
- Présentation des principes et pratiques ITIL.
- Complémentarité entre DevOps et ITIL.

> **Recherche et expérimentation :** analyser les pratiques existantes de NovaTech et expliquer comment Agile, Lean, ITSM et DevOps peuvent contribuer à améliorer son fonctionnement.

#### Guide de recherche — Module 3

**Questions de recherche**

- **Q3.1** - Quelles sont les quatre valeurs du Manifeste agile ?
- **Q3.2** - Qu'est-ce que l'ITSM, et à quoi sert ITIL ?

- **Q3.3** - Scrum garantit-il à lui seul des mises en production fiables ? Pourquoi ?
- **Q3.4** - Quels gaspillages au sens du Lean repérez-vous dans le processus de NovaTech ?

- **Q3.5** - Comment concilier une gestion des changements de type ITIL (validations, comité de changement) avec des livraisons petites et fréquentes ?
- **Q3.6** - Que traite le Lean que les outils de CI ne résolvent pas ?

- **Q3.7** - Proposez une organisation de NovaTech combinant Agile, Lean, ITSM et DevOps : qui décide de quoi, avec quels risques ?
- **Q3.8** - ITIL 4 et DevOps : convergence ou concurrence ? Comparez au moins deux sources et précisez leurs dates.

**Consignes d'expérimentation**

- **Objectif :** montrer comment Agile, Lean, ITSM et DevOps se complètent face aux problèmes de NovaTech.
- **Matériel et données :** dossier NovaTech, votre diagnostic du module 1, votre VSM du module 2.

**Étapes :**

1. Choisir quatre difficultés de NovaTech issues de votre diagnostic.
2. Pour chacune, indiquer l'apport possible d'Agile, de Lean, de l'ITSM et de DevOps.
3. Remplir la matrice : problème / approche / justification / risque.
4. Identifier au moins une tension entre deux approches et proposer un compromis.
5. Faire relire la matrice par un autre membre, qui la reformule sans la lire.

- **Critère de réussite :** quatre problèmes traités, chaque choix justifié par une source ou un fait du dossier, au moins un risque par approche.
- **Trace dans le dépôt :** matrice dans `recherches/module-03/synthese.md`.
- **Limites à documenter :** analyse documentaire, sans observation d'une organisation réelle.

---

## Jour 2 - Culture DevOps, collaboration et automatisation

**Objectif de la journée :** comprendre les transformations culturelles et organisationnelles nécessaires à DevOps et expérimenter les principales pratiques techniques, notamment Git, CI/CD, DevSecOps et Infrastructure as Code.

### Module 4 - Culture, organisation et collaboration DevOps

#### 4.1. Comprendre la culture DevOps

- Définition de la culture organisationnelle.

#### 4.2. Découvrir le modèle CALMS

**Culture - Culture collaborative**

**Automation - Automatisation**

**Lean - Optimisation des flux**

**Measurement - Mesure**

**Sharing - Partage**

#### 4.3. Accompagner les changements culturels et organisationnels

- Identifier les freins au changement.
- Comprendre les comportements favorables et défavorables à DevOps.
- Apprentissage et désapprentissage des anciennes pratiques.
- Développer les compétences techniques et humaines.
- Rôles et responsabilités des différents acteurs.
- Leadership et accompagnement des équipes.
- Organisation des équipes et modèles de collaboration.
- Commencer une transformation DevOps à partir de l'existant.

#### 4.4. Découvrir le fonctionnement quotidien des équipes DevOps

- Activités et responsabilités quotidiennes.
- Organisation des tâches avec Kanban.
- Synchronisation et coordination entre les équipes.
- Revues de travail et rétrospectives.
- Gestion des incidents et retours d'expérience.
- Communication et collaboration avec ChatOps.
- Partage des connaissances et documentation technique.
- Amélioration continue du fonctionnement collectif.

> **Recherche et expérimentation :** organiser le fonctionnement d'une équipe DevOps chez NovaTech, mettre en place un tableau Kanban, définir les responsabilités et simuler une revue d'incident collaborative.

#### Guide de recherche - Module 4

**Questions de recherche**

- **Q4.1** - Que signifient les cinq lettres de CALMS ? Donnez un exemple concret pour chacune.
- **Q4.2** - Qu'est-ce qu'une revue d'incident sans blâme ?

- **Q4.3** - Quels freins culturels identifiez-vous chez NovaTech, et comment pourrait-on les observer concrètement ?
- **Q4.4** - Qu'est-ce que la sécurité psychologique, et pourquoi conditionne-t-elle l'apprentissage après un incident ?

- **Q4.5** - Comment mesurer un changement culturel sans se limiter à un questionnaire de satisfaction ?
- **Q4.6** - ChatOps : dans quels cas une notification aide-t-elle l'équipe, et dans quels cas nuit-elle à son attention ?

- **Q4.7** - Comparez deux modèles d'organisation (équipe DevOps dédiée, équipes produit autonomes, Team Topologies, SRE…) et recommandez-en un pour NovaTech.
- **Q4.8** - Comment faire évoluer une culture sans l'imposer : quel rôle pour le leadership, et que faire si un acteur clé résiste ?

**Consignes d'expérimentation**

- **Objectif :** appliquer CALMS à NovaTech, organiser le travail de l'équipe et vivre une revue d'incident sans blâme (TP 3).
- **Matériel et données :** `donnees-novatech/03_Incident_fictif.md`, tableau Kanban, CI fournie (notification ChatOps simulée).

**Étapes :**

1. Pour chacune des cinq dimensions CALMS, relier un problème NovaTech à une action, un responsable et un indicateur.
2. Simuler une revue d'incident sans blâme : faits, chronologie, impact, hypothèses, actions avec propriétaire.
3. Écrire les politiques du tableau Kanban (définition de « Terminé », règle de revue, limite WIP).
4. Concevoir un message ChatOps : événement CI → notification dans un canal → action humaine ou ticket ; préciser l'information utile, le risque de bruit et la confidentialité.
5. Repérer dans la CI fournie l'étape ChatOps simulée ; vous l'observerez en échec au module 5.

- **Critère de réussite :** les cinq dimensions traitées avec une mesure chacune, revue d'incident sans recherche de coupable, actions assignées, au moins un risque de sécurité abordé.
- **Trace dans le dépôt :** `novatech/analyse-calms.md`, `experiences/retour-incident.md`, `experiences/chatops.md`, `recherches/module-04/synthese.md`.
- **Limites à documenter :** incident fictif sans logs ni métriques ; notification ChatOps simulée, sans canal de messagerie réel.

### Module 5 - Automatisation et chaîne de livraison DevOps

#### 5.1. Comprendre les objectifs de l'automatisation

- Pourquoi automatiser dans une démarche DevOps ?
- Identifier les activités pouvant être automatisées.
- De la User Story à la mise en production.
- Comprendre le cycle de vie d'une application.
- Limites et risques d'une automatisation mal maîtrisée.

#### 5.2. Collaborer et gérer le code source avec Git

- Principes du versionnement.
- Introduction à Git, GitHub et GitLab.
- Repository local et repository distant.
- Commits, branches, merge et historique des modifications.
- Pull requests et merge requests.

#### 5.3. Découvrir l'intégration et la livraison continues

**Intégration continue - CI**

- Définition et objectifs de la CI.
- Comprendre le fonctionnement d'un pipeline.

**Livraison continue et déploiement continu - CD**

- Définition et objectifs de la CD.
- Différence entre livraison continue et déploiement continu.
- Stratégies de déploiement et retour arrière.
- Risques liés aux mises en production.

#### 5.4. Découvrir DevSecOps

- Principes et objectifs de DevSecOps.
- Sécurisation des pipelines CI/CD.
- Introduction aux pratiques de sécurité dans la chaîne de livraison.

#### 5.5. Explorer l'écosystème des outils DevOps

- Outils de gestion du code source.
- Outils d'intégration et de livraison continues.
- Outils de construction et de stockage des artefacts.
- Outils de gestion des configurations.
- Outils de conteneurisation.
- Outils d'automatisation de l'infrastructure.
- Outils de supervision et d'observabilité.
- Outils de collaboration et ChatOps.
- Critères de sélection et d'intégration des outils.

> **Recherche et expérimentation :** travailler en équipe avec GitHub ou GitLab, versionner une application, créer un pipeline CI, automatiser des tests et observer la détection puis la correction d'une erreur.

#### Guide de recherche - Module 5

**Questions de recherche**

- **Q5.1** - Qu'est-ce qu'un commit, une branche et une pull request (ou merge request) ?
- **Q5.2** - Que fait un pipeline d'intégration continue, et qu'est-ce qui le déclenche ?

- **Q5.3** - Que prouve une CI verte, et que ne prouve-t-elle pas ?
- **Q5.4** - Différence entre livraison continue et déploiement continu : laquelle conviendrait à NovaTech aujourd'hui, et pourquoi ?

- **Q5.5** - Quels contrôles DevSecOps ajouteriez-vous au pipeline, et que laisseraient-ils passer ?
- **Q5.6** - Quelles tâches de NovaTech automatiser en premier, et lesquelles ne pas automatiser ? Justifiez par le coût, le risque et la fréquence.

- **Q5.7** - Concevez une stratégie de déploiement avec retour arrière (blue/green, canary, feature flags) adaptée au module de paiement de NovaTech.
- **Q5.8** - Quels risques pèsent sur la chaîne CI/CD elle-même (voir l'OWASP Top 10 CI/CD Security Risks) et comment les réduire ?

**Consignes d'expérimentation**

- **Objectif :** travailler à trois avec Git et observer le feedback d'une CI : rouge, correction, vert (TP 4).
- **Matériel et données :** `application/` (tests Python sans dépendance), CI déjà présente à la racine du dépôt, plateforme GitHub ou GitLab.

**Étapes :**

1. Depuis `application/`, lancer `python -m unittest discover -s tests -v` et noter le résultat.
2. Créer une branche, remplacer l'attendu `38.0` par `39.0` dans `application/tests/test_app.py`, relancer les tests et constater l'échec.
3. Pousser la branche et ouvrir une PR/MR ; observer le pipeline rouge et la notification ChatOps simulée.
4. Restaurer l'attendu, pousser à nouveau et obtenir un pipeline vert ; faire relire la PR/MR par un autre membre avant la fusion.
5. Ajouter un test (par exemple quantité négative refusée) dans une nouvelle PR/MR relue.
6. Facultatif : dans une branche jetable, committer un jeton manifestement factice et observer l'échec du job `secrets` ; ne jamais utiliser un vrai jeton.

- **Critère de réussite :** deux runs identifiables (rouge puis vert) avec leur explication, au moins une revue par membre, aucune affirmation de déploiement en production.
- **Trace dans le dépôt :** `experiences/ci-tests.md`, liens des runs et des PR/MR dans `preuves/`, `recherches/module-05/synthese.md`.
- **Limites à documenter :** une CI de tests n'est ni une livraison continue ni un déploiement continu ; si les runners sont indisponibles, appliquer le plan B (tests locaux et YAML relu) et écrire « CI distante non démontrée ».

### Module 6 — Infrastructure as Code 

#### 6.1. Comprendre l'Infrastructure as Code (IaC)

- Définition et objectifs de l'Infrastructure as Code.
- Infrastructure traditionnelle et infrastructure automatisée.
- Limites de la configuration manuelle.
- Approches déclaratives et impératives.

#### 6.2. Découvrir les outils et approches IaC

- Terraform et OpenTofu : outils IaC de provisionnement, qui décrivent de façon déclarative les ressources d'infrastructure et gèrent leur état.
- Ansible : automatisation et gestion de configuration, fréquemment utilisé dans une démarche IaC.
- Docker et Docker Compose : conteneurisation et description d'environnements applicatifs ; ils s'inscrivent dans une démarche IaC sans être des outils IaC au même titre que Terraform ou OpenTofu.
- Panorama des principales catégories d'outils IaC.
- Introduction au principe de Pipeline as Code.
- Utilisation de Git pour gérer les fichiers d'infrastructure.
- Découvrir l'approche GitOps

> **Nuance importante :** Docker et Docker Compose peuvent s'inscrire dans une démarche Infrastructure as Code : l'environnement applicatif (image, services, ports, variables) est décrit dans des fichiers versionnés, relus et rejouables. Ils ne sont pas pour autant des outils IaC au même titre que Terraform ou OpenTofu, qui provisionnent et gèrent des ressources d'infrastructure (réseaux, machines, services cloud) avec un fichier d'état et un plan de changements.

#### 6.3. Intégrer l'IaC dans une démarche DevOps

- Intégration de l'IaC dans un pipeline CI/CD.
- Sécurité des configurations et gestion des secrets.
- Précautions avant application des changements en production.

> **Recherche et expérimentation :** créer et versionner une configuration d'environnement, expérimenter son exécution ou sa validation et expliquer comment l'IaC contribue à la reproductibilité et à la fiabilité des environnements.

#### Guide de recherche - Module 6

**Questions de recherche**

- **Q6.1** - Qu'est-ce que l'Infrastructure as Code ?
- **Q6.2** - Quelle différence faites-vous entre une approche déclarative et une approche impérative ?

- **Q6.3** - Qu'est-ce que l'idempotence ? Qu'avez-vous observé en relançant `docker compose up`, et en quoi est-ce différent de l'idempotence d'un outil IaC comme Terraform ou OpenTofu ?
- **Q6.4** - Docker Compose est-il un outil IaC au même titre que Terraform ou OpenTofu ? En quoi s'inscrit-il malgré tout dans une démarche IaC, et pourquoi ne suffit-il pas à gérer une infrastructure cloud ?

- **Q6.5** - Pourquoi les fichiers d'état (par exemple `terraform.tfstate`) et les secrets exigent-ils des précautions ?
- **Q6.6** - Comparez OpenTofu/Terraform, Ansible et Docker Compose : usage, gestion d'état, idempotence, limites.

- **Q6.7** - Comment intégreriez-vous l'IaC dans un pipeline (plan, revue, application) avec une validation avant la production ?
- **Q6.8** - Qu'est-ce que la dérive de configuration, et comment la détecter et la corriger durablement ?

**Consignes d'expérimentation**

- **Objectif :** versionner et vérifier un environnement applicatif décrit as code avec Docker Compose (démarche IaC), et le distinguer du provisionnement d'infrastructure réalisé par des outils IaC comme Terraform ou OpenTofu (TP 5).
- **Matériel et données :** `application/compose.yaml` et `application/Dockerfile` ; Docker si disponible.

**Étapes :**

1. Option A (Docker disponible) : depuis `application/`, lancer `docker compose config`, puis `docker compose up --build -d`.
2. Vérifier `http://127.0.0.1:8000/health`, `docker compose ps` (état `healthy`), `docker compose logs` et `docker compose exec novatech-demo id` (utilisateur non root).
3. Relancer `docker compose up -d` et observer que rien n'est recréé (comportement idempotent), puis `docker compose down`.
4. Option B (pas de Docker) : analyser le `Dockerfile` et le `compose.yaml` (port, variable d'environnement, utilisateur, contrôle de santé) et faire relire l'analyse par un pair, sans annoncer d'exécution.
5. Remplir un tableau comparatif Compose / Ansible / OpenTofu : périmètre, état, idempotence, secrets, contrôles avant application.
6. Vérifier que le `.gitignore` exclut les fichiers d'état et de secrets, et expliquer pourquoi.

- **Critère de réussite :** sortie réelle des commandes (ou analyse explicitement non exécutée) ; explication claire de la nuance : Docker Compose s'inscrit dans une démarche IaC sans être un outil IaC de provisionnement comme Terraform ou OpenTofu.
- **Trace dans le dépôt :** `infrastructure/README.md`, sorties de validation dans `preuves/`, `recherches/module-06/synthese.md`.
- **Limites à documenter :** environnement local uniquement ; aucune ressource cloud n'est créée.

---

## Jour 3 - Mesurer, améliorer et adopter DevOps en entreprise

**Objectif de la journée :** comprendre comment évaluer la performance d'une démarche DevOps, améliorer les processus et définir une stratégie d'adoption progressive adaptée à une organisation.

### Module 7 - Mesure de la performance, fiabilité et amélioration continue

#### 7.1. Comprendre la mesure de performance DevOps

- Pourquoi mesurer la performance ?
- Définir des indicateurs pertinents.
- Différencier indicateurs métier, techniques et opérationnels.
- Relier les objectifs DevOps aux résultats de l'entreprise.
- Exploiter les métriques dans une démarche d'amélioration continue.
- Construire des tableaux de bord et des reportings.
- Comprendre les limites et les risques d'une mauvaise interprétation des indicateurs.

#### 7.2. Découvrir les métriques DORA

- Présentation de la démarche de recherche DORA.
- Comprendre les indicateurs de performance de livraison logicielle.
- Fréquence des déploiements (Deployment Frequency).
- Délai de réalisation des changements (Change Lead Time).
- Taux d'échec des changements (Change Fail Rate).
- Temps de restauration après échec d'un déploiement (Failed Deployment Recovery Time).
- Taux de reprises de déploiement (Deployment Rework Rate).
- Comprendre l'évolution des métriques DORA.
- Interpréter les résultats dans leur contexte.
- Utiliser les indicateurs pour orienter les améliorations.

#### 7.3. Développer la fiabilité et l'observabilité

- Introduction à la supervision et à l'observabilité.
- Comprendre les journaux, les métriques et les traces.
- Détection des anomalies et des incidents.
- Analyse des problèmes en production.
- Introduction à la résilience des systèmes.
- Préparation et gestion des incidents.
- Retours d'expérience et analyse des causes.

#### 7.4. Améliorer les processus avec Lean et DevOps

- Identifier les flux de valeur.
- Utiliser la Value Stream Mapping.
- Analyser les délais et les goulots d'étranglement.
- Appliquer la théorie des contraintes.
- Exploiter Kanban pour visualiser et optimiser le travail.
- Utiliser le cycle PDCA pour améliorer un processus.
- Introduction à l'Improvement Kata.
- Construire des boucles de feedback.
- Mesurer l'efficacité des actions d'amélioration.

> **Recherche et expérimentation :** analyser des données de livraison de NovaTech, calculer des métriques DORA, identifier les points de faiblesse et proposer des actions d'amélioration mesurables.

#### Guide de recherche - Module 7

**Questions de recherche**

- **Q7.1** - Quelles sont les cinq métriques DORA actuelles ? Définissez chacune en une phrase.
- **Q7.2** - Quelle différence faites-vous entre logs, métriques et traces ?

- **Q7.3** - Calculez les cinq métriques sur `04_Deploiements_fictifs.csv` en donnant le numérateur, le dénominateur, l'unité et la période.
- **Q7.4** - Pourquoi la médiane du délai de livraison peut-elle être plus parlante que la moyenne ?

- **Q7.5** - Pourquoi le temps de restauration DORA n'est-il pas le MTTR de toutes les pannes ?
- **Q7.6** - Quelles conclusions ne peut-on pas tirer de ces données fictives ? Citez au moins trois limites.

- **Q7.7** - Comment éviter qu'une métrique devienne un objectif manipulable (loi de Goodhart) ? Proposez des garde-fous.
- **Q7.8** - Concevez un tableau de bord combinant DORA, indicateurs métier et observabilité pour NovaTech : quelles décisions permettrait-il de prendre ?

**Consignes d'expérimentation**

- **Objectif :** calculer et interpréter les métriques DORA, puis proposer une amélioration mesurable (TP 6).
- **Matériel et données :** `donnees-novatech/04_Deploiements_fictifs.csv` et `05_Notice_des_donnees.md`, un tableur ou un petit script.

**Étapes :**

1. Déterminer le nombre de déploiements et exprimer la fréquence par 30 jours et par jour.
2. Calculer chaque délai `deployed_at - committed_at`, puis la moyenne et la médiane, en heures.
3. Calculer le change fail rate et le deployment rework rate (numérateur / dénominateur).
4. Calculer la moyenne et la médiane du temps de restauration des déploiements défaillants.
5. Proposer une boucle PDCA : hypothèse, changement limité, mesure et condition de décision.
6. Rédiger au moins trois limites, dont l'absence de preuve d'effet réel de vos propositions.

- **Critère de réussite :** calculs justes et vérifiables dans le fichier de calcul, unités et période explicites, interprétation prudente.
- **Trace dans le dépôt :** `novatech/indicateurs-dora.md`, fichier de calcul (tableur ou script) dans `novatech/`, `recherches/module-07/synthese.md`.
- **Limites à documenter :** jeu synthétique de 20 déploiements ; pas de comparaison avant/après possible.

### Module 8 - Construire une démarche d'adoption DevOps en entreprise

#### 8.1. Évaluer la situation existante

#### 8.2. Définir une stratégie de transformation DevOps

#### 8.3. Construire une feuille de route DevOps

#### 8.4. Présenter et défendre une démarche DevOps

- Structurer un diagnostic de l'existant.
- Justifier les pratiques et outils retenus.
- Présenter les expérimentations réalisées.
- Démontrer les améliorations possibles.
- Expliquer les bénéfices attendus et les risques.
- Défendre une stratégie de transformation devant des décideurs.
- Identifier les limites et les prochaines étapes.

> **Recherche et expérimentation :** élaborer une feuille de route de transformation DevOps pour NovaTech et défendre les recommandations à partir des recherches, des expérimentations et des résultats obtenus au cours des trois jours.

#### Guide de recherche — Module 8

**Questions de recherche**

- **Q8.1** - Pourquoi ne pas commencer une transformation DevOps en installant tous les outils ?
- **Q8.2** - Qui sont les parties prenantes de la transformation chez NovaTech, et quelles sont leurs attentes ?

- **Q8.3** - Quels critères retiendriez-vous pour choisir un projet pilote ?
- **Q8.4** - Comment prioriser les actions selon leur valeur, leur effort et leur risque ? Appliquez la méthode à trois actions.

- **Q8.5** - Quels risques et quelles résistances anticipez-vous, et comment les traiter ?
- **Q8.6** - Au bout de 30 jours, comment décider de poursuivre, d'ajuster ou d'arrêter un pilote ?

- **Q8.7** - Construisez une feuille de route 30/60/90 jours cohérente avec vos expérimentations, avec indicateurs et critères d'arrêt.
- **Q8.8** - Comment adapter la gouvernance ITSM et la sécurité à l'échelle de l'organisation sans freiner les équipes ?

**Consignes d'expérimentation**

- **Objectif :** construire et défendre une feuille de route réaliste pour NovaTech (TP 7 et soutenance).
- **Matériel et données :** l'ensemble de vos synthèses, diagnostics, expérimentations et indicateurs.

**Étapes :**

1. Résumer l'état initial : culture, processus, outils, sécurité, contraintes.
2. Lister les actions par dimension (culture, processus, technique, sécurité) et les prioriser selon valeur, effort et risque.
3. Pour chaque action : constat ou hypothèse, propriétaire, dépendance, effort estimé, risque, métrique et critère de succès.
4. Répartir les actions sur 30, 60 et 90 jours ; prévoir les points de décision et les critères d'arrêt.
5. Relier chaque recommandation à une expérimentation réalisée ou à une source, et signaler ce qui n'a pas été testé.
6. Préparer les slides 9 et 10 et répéter la soutenance (chaque membre présente et répond).

- **Critère de réussite :** actions réalistes et cohérentes avec les essais réalisés, hypothèses budgétaires explicites.
- **Trace dans le dépôt :** `novatech/feuille-de-route.md`, `presentation/soutenance-10-slides.md`, `recherches/module-08/synthese.md`.
- **Limites à documenter :** proposition non mise en œuvre ; effets attendus et non mesurés.

---

## Exigences communes pour chaque synthèse de module

Chaque `recherches/module-XX/synthese.md` contient : définitions reformulées ; réponses numérotées aux questions traitées ; références vérifiables avec date de consultation ; comparaison de sources et limites ; illustration d'entreprise ; expérimentation ou analyse documentée ; lien explicite avec un problème de NovaTech ; preuves (fichiers, captures, liens de commits, runs) ; rôles et apports de chacun ; contribution de l'IA vérifiée ; une question ouverte. **Ne jamais inventer une expérimentation non réalisée.**

## Récapitulatif des traces attendues

| Module | Expérimentation | Traces dans le dépôt |
|---|---|---|
| 1 | Jeu de rôles et diagnostic (TP 1) | `novatech/diagnostic.md` |
| 2 | VSM et tableau Kanban (TP 2) | `novatech/value-stream-map.md`, lien Kanban |
| 3 | Matrice Agile / Lean / ITSM / DevOps | `recherches/module-03/synthese.md` |
| 4 | CALMS, revue d'incident, ChatOps (TP 3) | `novatech/analyse-calms.md`, `experiences/retour-incident.md`, `experiences/chatops.md` |
| 5 | Git à trois, CI rouge puis verte (TP 4) | `experiences/ci-tests.md`, `preuves/` |
| 6 | Environnement as code (TP 5) | `infrastructure/README.md`, `preuves/` |
| 7 | Métriques DORA et PDCA (TP 6) | `novatech/indicateurs-dora.md`, fichier de calcul |
| 8 | Feuille de route et soutenance (TP 7) | `novatech/feuille-de-route.md`, `presentation/soutenance-10-slides.md` |

Chaque module a aussi sa synthèse : `recherches/module-01/synthese.md` à `module-08/synthese.md`.
