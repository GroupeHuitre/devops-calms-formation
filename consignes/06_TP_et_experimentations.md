# Cahier de travaux pratiques et d'expérimentations 

Chaque expérimentation doit être documentée dans `experiences/` : **objectif, hypothèse, prérequis, procédure, résultat réellement observé, preuve et limites**. Ne pas publier de données sensibles dans les captures ou logs.

Ces TP détaillent les consignes d'expérimentation résumées pour chaque module dans `consignes/02_Programme_recherches_8_modules.md` (TP 1 → module 1, TP 2 → module 2, TP 3 → module 4, TP 4 → module 5, TP 5 → module 6, TP 6 → module 7, TP 7 → module 8 ; le module 3 s'appuie sur une matrice comparative, sans TP dédié).

## TP 1 - Conflit Dev/Ops, perspective Business/IT 

**Situation :** la direction souhaite une promotion commerciale ; le développement veut livrer vite ; l'exploitation veut éviter les incidents ; la sécurité demande une revue. Distribuer un rôle à chacun des trois membres, puis faire tourner les rôles.

**Travail :** décrire objectifs, frictions, passage de relais, risques Business et IT ; proposer un fonctionnement où les fonctions participent dès la conception. Distinguer un fait du dossier NovaTech d'une hypothèse non encore étayée.

**Preuve :** `novatech/diagnostic.md` et une note de décision. **Critère :** au moins trois causes possibles, une pièce manquante par cause, deux propositions reliant coopération et valeur métier.

## TP 2 - Three Ways, théorie des contraintes et VSM 

**Source :** `donnees-novatech/02_Processus_actuel.csv`.

1. Représenter dans l'ordre : spécification → développement → revue → tests → validation → déploiement.
2. Relever pour chaque étape le temps actif et l'attente. Calculer temps actif total, attente totale, délai total et proportion d'attente.
3. Identifier la **plus longue attente**, sans la déclarer automatiquement « contrainte systémique » sans données de capacité/débit.
4. Imaginer une mesure de feedback plus précoce et un essai d'amélioration limité.
5. Classer les actions proposées dans **Flow**, **Feedback**, **Continual Learning & Experimentation**.
6. Créer le tableau Kanban de l'équipe (une carte par livrable), expliciter « Terminé » et le WIP si utile.

**Preuve :** `novatech/value-stream-map.md`, une issue d'expérimentation et une capture ou un lien de tableau Kanban. **Critère :** calculs corrects, distinction observation/hypothèse, expérience falsifiable.

## TP 3 - CALMS, organisation, DevSecOps, ChatOps 

1. Pour les cinq dimensions **CALMS**, lier un problème concret à une action, un responsable et un indicateur.
2. Simuler une revue d'incident **sans blâme** : faits, impact, hypothèses, mesures d'amélioration et propriétaires des actions.
3. **ChatOps :** construire le schéma de message : événement CI → notification dans un canal → action humaine ou ticket. Définir l'information nécessaire, le risque de bruit et la confidentialité. La CI fournie contient une **notification ChatOps simulée** (étape « Notification ChatOps simulée » sur GitHub, job `notification_chatops` sur GitLab) qui s'affiche uniquement en cas d'échec, sans webhook externe : vous l'observerez au TP4 et la critiquerez (information utile ? bruit ? destinataire ?).
4. **DevSecOps « shift left » :** la CI fournie lance aussi une **recherche de secrets** (gitleaks, job `secrets`). Expliquer ce qu'elle détecte et ce qu'elle ne couvre pas (dépendances vulnérables, droits du pipeline, secrets déjà diffusés, etc.). Observer aussi le `Dockerfile` : utilisateur non root, contrôle de santé ; justifier ces choix.

**Preuves :** `novatech/analyse-calms.md`, `experiences/chatops.md`, `experiences/retour-incident.md`. **Critère :** les cinq dimensions et au moins un risque sécurité sont réellement abordés.

## TP 4 - Git, tests et CI 

**Préparation :** le dossier `application/` et la CI sont déjà présents dans votre dépôt (créé depuis le dépôt modèle) ; voir `application/README.md`. Une seule plateforme GitHub ou GitLab par groupe. Tous les membres participent aux modifications/revues.

**Pièges fréquents :** lancer les tests **depuis le dossier `application/`** (depuis la racine du dépôt, Python ne trouve pas le module `app`) ; sous Windows, si `python` n'est pas reconnu, essayer `py` ; dans Windows PowerShell 5.1, utiliser `curl.exe` (et non `curl`, qui est un alias d'`Invoke-WebRequest`) ou un navigateur.

1. Depuis `application/`, lancer :

   ```bash
   python -m unittest discover -s tests -v
   ```

2. Décrire le sens d'une **suite verte** (les tests fournis passent) et ce qu'elle ne garantit pas (absence de défauts, conformité complète, sécurité de production).
3. Dans une branche, modifier volontairement l'attendu `38.0` en `39.0` dans `application/tests/test_app.py`. Tester. Consigner l'échec.
4. Vérifier que la CI déjà présente à la racine s'exécute : `.github/workflows/ci.yml` sur GitHub (onglet Actions), `.gitlab-ci.yml` sur GitLab (menu Build > Pipelines). Pousser la branche, ouvrir une PR/MR et demander une revue à un autre membre.
5. Observer le run **en échec** si un runner est disponible. Restaurer l'attendu, relancer les tests et obtenir un nouveau run **réussi**. Conserver deux liens de run (ou leurs logs si non accessibles publiquement).
6. Ajouter une petite modification documentée (ex. test de quantité négative), avec commit et revue ; relever les contributions des trois membres.
7. **Recherche de secrets (facultatif, dans une branche jetable) :** committer un faux jeton manifestement factice, par exemple `GITHUB_TOKEN=ghp_` suivi de 36 caractères inventés, observer l'échec du job `secrets`, puis supprimer la branche. Ne jamais utiliser un vrai jeton. Équivalent local si Docker est disponible : `docker run --rm -v "$PWD:/repo" ghcr.io/gitleaks/gitleaks:latest git /repo --redact`.

**Plan B si runners indisponibles :** exécuter les tests localement, conserver les logs et publier un pipeline YAML soumis à revue ; annoncer explicitement « CI distante non démontrée ».

**Preuves :** commit(s), revue(s), pipeline, résultats rouges/verts, causes et corrections dans `experiences/ci-tests.md`. **Critère :** démontrer et expliquer le feedback d'une modification défaillante.

## TP 5 - Environnement versionné avec Docker Compose (démarche IaC)

**À retenir :** Docker et Docker Compose peuvent s'inscrire dans une démarche Infrastructure as Code (environnement décrit dans des fichiers versionnés et rejouables), sans pour autant être des outils IaC au même titre que Terraform ou OpenTofu, qui provisionnent et gèrent des ressources d'infrastructure avec un état.

**Option A - Docker disponible :** depuis `application/`, lancer `docker compose config`, puis `docker compose up --build -d` et consulter `http://127.0.0.1:8000/health`. Vérifier `docker compose ps` (l'état doit passer à `healthy` après quelques secondes grâce au `HEALTHCHECK`), `docker compose logs` et `docker compose exec novatech-demo id` (utilisateur non root). Relancer `docker compose up -d` et observer que rien n'est recréé (idempotence). Finir par `docker compose down`.

**Option B - Docker indisponible :** analyser le `Dockerfile` et `compose.yaml`, expliquer le mappage de port, la variable d'environnement, la reproductibilité attendue, les risques et les vérifications à effectuer ; faire relire le fichier par un pair. Ne pas déclarer une exécution qui n'a pas eu lieu.

**Complément de recherche :** comparer Compose (description d'environnement applicatif, utilisée dans une démarche IaC), Ansible (configuration/automatisation) et OpenTofu/Terraform (outils IaC de provisionnement : gestion déclarative des ressources), leurs états, idempotence, gestion des secrets et contrôles avant application.

**Preuve :** `infrastructure/README.md`, fichiers versionnés, sortie réelle de validation si exécutée et limites. **Critère :** expliquer pourquoi Compose s'inscrit dans une démarche IaC sans être un outil IaC de provisionnement comme Terraform/OpenTofu, et le besoin de protéger les fichiers d'état.

## TP 6 - DORA à cinq métriques et PDCA

**Source :** `donnees-novatech/04_Deploiements_fictifs.csv` et notice associée.

1. Déterminer le nombre de déploiements sur la période : exprimer la fréquence **par 30 jours** et, éventuellement, par jour.
2. Calculer chaque lead time comme `deployed_at - committed_at`, puis la **moyenne** et la **médiane**. Expliciter l'unité.
3. Calculer le change fail rate = déploiements ayant provoqué une intervention / nombre de déploiements.
4. Calculer le deployment rework rate = déploiements imprévus de correction / déploiements totaux.
5. Calculer la moyenne et la médiane des durées de restauration associées aux déploiements défaillants.
6. Proposer une boucle **Plan – Do – Check – Act** : hypothèse de réduction des attentes, changement limité, mesure observée et condition de décision.
7. Présenter au moins trois limites du jeu fictif, y compris l'absence de preuve d'un effet réel de vos propositions.

**Fichier de calcul :** réaliser les calculs dans un tableur (`novatech/calcul-dora.xlsx` ou `.ods`) ou un petit script versionné dans `novatech/` ; le fichier doit montrer les formules ou le code, pas seulement les résultats.

**Preuve :** `novatech/indicateurs-dora.md` avec calculs explicites, interprétation prudente et proposition PDCA, et le fichier de calcul.

## TP 7 - Stratégie d'adoption en entreprise 

Rédiger la feuille de route NovaTech à **30 / 60 / 90 jours**, par dimension (culture, processus, technique et sécurité). Pour chaque action : constat ou hypothèse, propriétaire, dépendance, effort estimé qualitativement, risque, métrique et critère de succès. Inclure les résistances au changement, les besoins de formation, les pratiques ITSM et les décisions managériales.

**Preuve :** `novatech/feuille-de-route.md` et slides 9–10. **Critère :** réalisme, cohérence avec les essais réalisés, et transparence des hypothèses budgétaires.


