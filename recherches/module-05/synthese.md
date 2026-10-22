# Module 05 - Automatisation, Git, CI/CD, outils

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q5.1 à Q5.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q5.1** - Qu'est-ce qu'un commit, une branche et une pull request (ou merge request) ?

Un commit est un enregistrement des modifications du code à un instant donné, avec un message qui explique ce qui a changé. Une branche est une ligne de travail parallèle, qui permet de développer sans toucher au code principal.

Une merge request (ou une pull request pour GitHub) sert au DevOps à présenter ses changements et leur raison, et permet la revue par les collaborateurs et la validation par les code owners.

Sources : https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Les-branches-en-bref et https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

- **Q5.2** - Que fait un pipeline d'intégration continue, et qu'est-ce qui le déclenche ?

Un pipeline de CI automatise la vérification d'un changement (tests, contrôles qualité/sécurité) dès qu'il est poussé ou proposé en pull request, pour donner un retour rapide vert/rouge (jaune pour les warnings) avant toute mise en production. C'est exactement ce que fait `ci.yml` dans notre dépôt actuel, à chaque push sur `main` ou à chaque PR. L'équivalent GitLab étant `.gitlab-ci.yml`.

- **Q5.3** - Que prouve une CI verte, et que ne prouve-t-elle pas ?

Une CI verte prouve que le code passe les tests et contrôles qui existent dans le pipeline. Elle ne prouve ni l'absence de bug non couvert par un test, ni le bon comportement en production réelle, ni que le déploiement se déroulera sans accroc.

- **Q5.4** - Différence entre livraison continue et déploiement continu : laquelle conviendrait à NovaTech aujourd'hui, et pourquoi ?

NovaTech devrait viser la livraison continue aujourd'hui : automatiser jusqu'à la préparation du déploiement, en gardant une validation humaine finale. Les conditions de confiance nécessaires au déploiement continu (rollback testé, monitoring, couverture de tests) ne sont pas encore réunies, comme l'a montré l'incident du 16/10.

Source : https://martinfowler.com/bliki/ContinuousDelivery.html

- **Q5.5** - Quels contrôles DevSecOps ajouteriez-vous au pipeline, et que laisseraient-ils passer ?

Chaque contrôle DevSecOps ajouté (SAST, SCA, scan d'image) élargit ce que le pipeline détecte automatiquement, mais aucun n'est exhaustif. Ensemble, ils réduisent le risque sans jamais prouver l'absence totale de vulnérabilité, ce qui justifie de garder aussi une revue humaine lors des merge requests (ou pull requests).

- **Q5.6** - Quelles tâches de NovaTech automatiser en premier, et lesquelles ne pas automatiser ? Justifiez par le coût, le risque et la fréquence.

NovaTech devrait automatiser en priorité les tâches répétitives et à risque limité (tests, scan de secrets, déploiements à faible risque, alertes de base), car leur fréquence rend le gain immédiat et sûr. Elle devrait laisser en décision humaine les tâches rares à fort enjeu (validation des changements majeurs, exceptions de sécurité), où une automatisation mal calibrée coûterait plus cher qu'elle ne ferait gagner.

- **Q5.7** - Concevez une stratégie de déploiement avec retour arrière (blue/green, canary, feature flags) adaptée au module de paiement de NovaTech.

Pour le module de paiement, une feature flag permettant une désactivation instantanée du nouveau code, combinée à un déploiement canary surveillé automatiquement, répond directement à la faiblesse révélée par l'incident du 16/10 (retour arrière non accessible). Le blue/green reste une option plus coûteuse, à mentionner comme piste future plutôt que comme solution immédiate, faute de budget cloud chez NovaTech.

- **Q5.8** - Quels risques pèsent sur la chaîne CI/CD elle-même (voir l'OWASP Top 10 CI/CD Security Risks) et comment les réduire ?

La chaîne CI/CD de NovaTech est déjà protégée sur un point (permissions minimales du token), mais reste exposée sur d'autres (image tierce non épinglée, pas de contrôle sur les workflows venant de forks). Réduire ces risques demande d'épingler les dépendances, de limiter les droits des pipelines au strict nécessaire et de garder une trace auditable des exécutions.

Source : OWASP, Top 10 CI/CD Security Risks, https://owasp.org/www-project-top-10-ci-cd-security-risks/

## 2. Concepts expliqués avec nos mots
**Point incontournable :** CI ≠ livraison continue ≠ déploiement continu

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [Pro Git - Les branches en bref](https://git-scm.com/book/fr/v2/Les-branches-avec-Git-Les-branches-en-bref) | Pro Git (Scott Chacon et Ben Straub) | 21/10/2026 | Un commit enregistre un instantané du code avec son auteur et son message. Une branche est un simple pointeur déplaçable vers un commit. | Les auteurs ne sont pas cités sur la page elle-même. Pas de date. |
| [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | GitHub | 21/10/2026 | Une pull request est une proposition de fusion de modifications, qui permet d'en discuter et de les relire avant de les intégrer. Les code owners sont sollicités automatiquement quand la PR est prête pour revue. | Documentation officielle, propre à GitHub. Pas de date. |
| [Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html) | Martin Fowler | 21/10/2026 | En livraison continue, le logiciel peut partir en production à tout moment, mais l'équipe décide quand. En déploiement continu, chaque changement validé part automatiquement. | Article de blog, mais référence reconnue. Publié le 30/05/2013, mis à jour le 12/08/2014. |
| [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) | OWASP Foundation (Daniel Krivelevich, Omer Gil, Ory Segal) | 21/10/2026 | Liste des 10 risques de la chaîne CI/CD, dont l'abus de la chaîne de dépendances, la gestion insuffisante des identités et accès, et le manque de journalisation. | Pas de date de publication sur la page. |

## 4. Exemple professionnel commenté

## 5. Expérimentation / analyse
**Piste :** CI rouge/verte, revues de code, sécurité du workflow
- Hypothèse :
- Protocole / méthode :
- Résultat observé ou simulation :
- Ce que ce résultat ne prouve pas :

## 6. Application à NovaTech
- Problème visé :
- Action envisagée :
- Indicateur et risque :

## 7. Preuves déposées
**Attendu :** Commits/MR/PR, captures des runs et limites
- Liens commits / MR / CI / fichiers :

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a corrigé l'orthographe des réponses, complété la Q5.1 (définitions du commit et de la branche) et vérifié chaque source (auteur, date, lien fonctionnel).

## 10. Questions ouvertes / blocages
