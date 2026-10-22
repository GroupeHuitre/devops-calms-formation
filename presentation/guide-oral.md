# Guide de l'oral - soutenance NovaTech

Timing : 10 min de présentation, soit **environ 1 min par slide**, puis 5 min de questions.

Les slides ne montrent que l'essentiel. Pour chaque slide, ce guide donne :
- **À l'écran :** ce que le public voit ;
- **À dire :** les repères pour l'oral, avec les détails qui ne sont pas sur la slide. Ce n'est pas un texte à lire mot à mot ;
- **Question possible :** une question du jury, avec une piste de réponse.

## Slide 01 - Qui sommes-nous ? Quelle est la mission de NovaTech ?
**Qui parle :** …
- **À l'écran :** nos 4 prénoms, la demande de la direction, le périmètre.
- **À dire :**
  - Chacun se présente en une phrase (prénom, rôle).
  - NovaTech : une plateforme de commerce en ligne fictive, avec une équipe Dev, une équipe Ops, une fonction sécurité et un responsable métier.
  - Notre rôle : jouer les consultants qui répondent à la direction avec des preuves, des options et un plan.
  - Le périmètre : tout a été fait en local, sans toucher à un vrai système.
- **Question possible :** comment vous êtes-vous organisés ? → rôles tournants, RACI, Kanban, une branche par module, PR relues par le PO.

## Sommaire
**Qui parle :** la même personne que la slide 01
- **À l'écran :** les 3 parties et les slides de chacune.
- **À dire :** une seule phrase, 15 secondes maximum. D'abord le contexte, puis notre démarche et nos tests, enfin nos résultats et notre proposition.

## Slide 02 - Diagnostic des problèmes Business, IT, culture et organisation
**Qui parle :** …
- **À l'écran :** le chiffre « 80 % », un constat par dimension, notre hypothèse.
- **À dire :**
  - Les 80 % : sur 110 h pour livrer un changement, 88 h sont de l'attente. C'est le chiffre à retenir.
  - Un fait par dimension, sans détailler.
  - L'incident du 16/10 : déploiement un vendredi à 16h45, retour arrière pas accessible, service rétabli au bout de 95 min.
  - Notre conclusion n'est qu'une hypothèse. Pour la prouver, il nous manque les logs, les métriques et la cause réelle de l'incident.
- **Question possible :** pourquoi ne pas conclure à un problème d'outils ? → la plus grosse attente (36 h de validation) vient d'une règle d'organisation, aucun outil ne la supprime.

## Slide 03 - Origine, définition et valeur de DevOps
**Qui parle :** …
- **À l'écran :** les 3 blocs (origine, définition, valeur) et le bandeau Knight Capital.
- **À dire :**
  - Origine : la présentation de Flickr en 2008 (« 10+ deploys per day »), puis le premier DevOpsDays à Gand en 2009.
  - Notre définition, sans citer d'outil : DevOps n'est ni un outil, ni un poste, ni une équipe.
  - Valeur : un exemple par angle. Business, livrer plus vite. IT, moins d'incidents. Équipes, moins de conflits.
  - Knight Capital : un déploiement manuel, un serveur oublié sur huit, plus de 460 M$ perdus en 45 minutes. C'est l'histoire qui marque.
- **Question possible :** DevOps, c'est un métier ? → non, c'est une façon de travailler partagée par tous.

## Slide 04 - Three Ways et CALMS appliqués à NovaTech
**Qui parle :** …
- **À l'écran :** les 3 voies et les 5 lettres CALMS, chacune avec une action.
- **À dire :**
  - Flow : en validant les changements chaque jour au lieu de par lots, le délai passerait de 110 h à 86 h. C'est une simulation, pas une mesure.
  - Feedback : des tests automatiques pour voir l'erreur avant le client.
  - Apprendre : une revue sans blâme après chaque incident.
  - CALMS : détailler 2 lettres seulement. Par exemple, la Culture (la réunion de crise du 16/10 n'a débouché sur rien) et le Sharing (l'Ops découvre les changements la veille).
- **Question possible :** quelle lettre de CALMS est prioritaire ? → la Culture : sans confiance, les autres ne tiennent pas.

## Slide 05 - Culture, Agile/Lean/ITSM, Kanban et ChatOps
**Qui parle :** …
- **À l'écran :** les 5 blocs.
- **À dire :**
  - Culture : sans sécurité psychologique, les erreurs sont cachées (Edmondson, 1999).
  - Agile décide quoi livrer, Lean chasse l'attente.
  - ITSM : on garde un contrôle, mais adapté au risque. Revue d'un collègue et CI pour les changements courants, comité seulement pour le paiement.
  - Kanban : montrer notre vrai tableau si on a le temps.
  - ChatOps : la CI ne prévient qu'en cas d'échec. On a testé un envoi vers un canal Discord.
- **Question possible :** ITIL et DevOps ne sont-ils pas incompatibles ? → plus avec ITIL 4, qui reprend des idées DevOps (voir notre Q3.8).

## Slide 06 - Git, CI/CD, DevSecOps et Infrastructure as Code
**Qui parle :** …
- **À l'écran :** le chemin d'un changement en 5 étapes.
- **À dire :**
  - Suivre les flèches. On crée une branche, on ouvre une PR relue par un collègue, la CI lance les tests, gitleaks cherche les secrets, et Docker Compose décrit l'environnement.
  - DevSecOps : la CI n'a que des droits de lecture, et l'application ne tourne pas en root.
  - Pour NovaTech, on recommande la livraison continue et pas encore le déploiement continu : il n'y a pas de retour arrière testé ni de surveillance.
- **Question possible :** Docker Compose, c'est de l'IaC ? → c'est une démarche IaC (un fichier versionné et rejouable), mais pas un outil de provisionnement comme Terraform.

## Slide 07 - Nos expérimentations : réussites, échecs, preuves
**Qui parle :** …
- **À l'écran :** réussites, échecs et preuves, en 3 blocs.
- **À dire :**
  - Réussites : un test cassé exprès (38 → 39), la CI passe au rouge (run #4) puis au vert après correction (run #5). Avec Docker, l'application est « healthy », la relance ne recrée rien et elle ne tourne pas en root.
  - Échecs, à dire franchement : la CI ne se lançait pas sur notre branche de test, et Docker et Python n'étaient pas installés partout.
  - Le test gitleaks et l'envoi Discord : donner le résultat s'il est connu, sinon dire qu'il reste à vérifier.
  - Anecdote si on a le temps : deux IP différentes dans les logs Docker montrent que le conteneur a son propre réseau.
- **Question possible :** qu'est-ce qu'une CI verte ne prouve pas ? → l'absence de bug non testé, ni le bon fonctionnement en production.

## Slide 08 - Cinq métriques DORA, observabilité, feedback et PDCA
**Qui parle :** …
- **À l'écran :** les 5 chiffres et les 4 étapes du PDCA.
- **À dire :**
  - Période : 20 déploiements fictifs, du 20/09 au 19/10/2026.
  - Les chiffres de vitesse : 20 déploiements en 30 jours, 55 h de lead time médian.
  - Les chiffres de stabilité : 15 % d'échecs, 10 % de déploiements de correction, 95 min de rétablissement médian.
  - Un chiffre seul ne juge pas une équipe : c'est l'évolution qui compte, et une métrique imposée comme objectif finit par être manipulée (loi de Goodhart).
  - Observabilité en une phrase : les logs disent ce qui s'est passé, les métriques montrent la tendance, les traces disent où ça bloque.
  - Le PDCA : tester la validation quotidienne pendant 2 semaines, viser moins de 12 h d'attente sans plus d'échecs, puis généraliser ou arrêter.
- **Question possible :** pourquoi la médiane plutôt que la moyenne ? → elle n'est pas faussée par quelques valeurs extrêmes.

## Slide 09 - Proposition de transformation NovaTech 30/60/90 jours
**Qui parle :** …
- **À l'écran :** le tableau culture / processus / outils sur 30, 60 et 90 jours.
- **À dire :**
  - Lire colonne par colonne : ce qu'on fait le premier mois, puis la suite.
  - Les indicateurs suivis à chaque étape : l'attente avant validation (36 h), le lead time (55 h), le temps de rétablissement.
  - Le critère d'arrêt : si les échecs augmentent ou si un incident vient du changement, on arrête.
  - Ce qui s'appuie sur nos tests (CI, Compose, ChatOps) et ce qui reste une proposition.
  - Aucun budget n'est inventé : les effectifs et le budget de NovaTech ne sont pas connus.
- **Question possible :** pourquoi ne pas tout faire tout de suite ? → trop de risques et de résistances, mieux vaut des petites réussites visibles.

## Slide 10 - Bilan, limites, décisions et apprentissages (dont IA)
**Qui parle :** chacun peut prendre un mot
- **À l'écran :** appris, décidé, limites, IA, et la recommandation.
- **À dire :**
  - Appris : la culture avant les outils, et une CI verte ne prouve pas l'absence de bug.
  - Décidé : bien s'organiser dès le premier jour, quitte à perdre un peu de temps au début, et toujours séparer les faits des hypothèses.
  - Limites : cas fictif, simulations non mesurées, tests en local seulement.
  - IA : dire honnêtement à quoi elle a servi.
  - Terminer sur la recommandation, puis ouvrir aux questions.

## Démo (si elle est demandée)

La consigne prévoit 5 min de démo en plus des slides : à vérifier avec le formateur.
1. Le dépôt : les branches et une PR relue.
2. Un test cassé puis corrigé, lancé depuis `application/`.
3. Les runs CI : rouge (#4), puis vert (#5).
4. `docker compose up --build -d`, puis `/health`, puis `docker compose ps` (healthy).
5. Relancer `docker compose up -d` (rien n'est recréé), puis `docker compose down`.

**En cas de bug :** montrer l'erreur et les captures déjà prises, sans cacher le problème.

## Rappels de la consigne
- Trois personnes prennent la parole.
- Chaque membre explique au moins un choix et répond seul à une question, sans IA.
- Chaque affirmation importante renvoie à une preuve ou une source (en bas de chaque slide).
