# Module 04 - Culture, CALMS, organisation, DevSecOps, ChatOps, Kanban

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q4.1 à Q4.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q4.1** - Que signifient les cinq lettres de CALMS ? Donnez un exemple concret pour chacune.

L'acronyme CALMS définit les cinq piliers fondamentaux de la culture DevOps. Inventé par John Willis et Damon Edwards en 2010 (puis complété par Jez Humble), il sert de cadre pour évaluer la maturité DevOps d'une organisation.

Voici la signification de chaque lettre accompagnée d'un exemple concret :

**C (Culture)**

La culture est le pilier le plus important. Elle vise à briser les silos entre les équipes de développement (Dev) et des opérations (Ops) pour instaurer un climat de confiance, de collaboration et de responsabilité partagée. Exemple concret : La mise en place de "Post-Mortems" non blâmants (Blameless Post-Mortems) après un incident de production. Au lieu de chercher un coupable, les équipes Dev et Ops se réunissent pour comprendre pourquoi le système a échoué et comment éviter que cela se reproduise.

**A (Automatisation)**

L'automatisation consiste à éliminer les tâches manuelles répétitives et sources d'erreurs afin de libérer du temps pour l'innovation et d'accélérer les déploiements. Exemple concret : L'utilisation d'un outil comme GitHub Actions ou GitLab CI pour exécuter automatiquement des tests unitaires et de sécurité à chaque fois qu'un développeur propose une modification de code.

**L (Lean)**

Inspiré du modèle de production de Toyota, le principe Lean en informatique consiste à éliminer le gaspillage, à travailler par petits lots (petites fonctionnalités) et à livrer de la valeur le plus rapidement possible au client. Exemple concret : Découper un projet de refonte d'application de six mois en micro-fonctionnalités déployées chaque semaine. Si une fonctionnalité déplaît aux utilisateurs, l'équipe s'en rend compte immédiatement et ajuste le tir sans avoir perdu des mois de travail.

**M (Measurement)**

Vous ne pouvez pas améliorer ce que vous ne mesurez pas. Ce pilier consiste à collecter des données sur les performances techniques (temps de réponse, taux d'erreur) et sur les processus (temps nécessaire pour déployer une idée). Exemple concret : Suivre les 4 métriques DORA (Délai de déploiement, Fréquence des déploiements, Taux d'échec des changements, Temps de restauration du service) sur un tableau de bord Grafana pour valider objectivement si l'équipe devient plus efficace au fil des mois.

**S (Sharing)**

Le partage renforce la culture en s'assurant que les retours d'expérience, les succès, les échecs et les outils soient accessibles à tous. Cela permet à l'ensemble de l'entreprise de progresser. Exemple concret : Organiser une réunion mensuelle de type "Tech Talk" ou "Brown Bag Lunch" où un membre de l'équipe Ops explique aux développeurs comment fonctionne la nouvelle infrastructure Cloud, afin que ces derniers écrivent du code mieux adapté à cet environnement. L’entretien d’un wiki d’entreprise avec des tutoriels, post mortems, et conseils s’inscrit dans cette démarche.

Sources :

https://itrevolution.com/articles/devops-culture-part-1/
https://www.sonatype.com/blog/principle-based-devops-frameworks-calms

- **Q4.2** - Qu'est-ce qu'une revue d'incident sans blâme ?

Une revue d’incident sans blâme est une analyse structurée menée après un dysfonctionnement ou une panne majeure, qui se concentre sur les causes systémiques et les processus plutôt que sur la recherche d'un coupable individuel. Le but est de produire de la documentation, et des actions tangibles permettant de réduire ou éliminer le risque d’incident, et accélérer sa remédiation.

Source :

https://sre.google/sre-book/postmortem-culture/

- **Q4.3** - Quels freins culturels identifiez-vous chez NovaTech, et comment pourrait-on les observer concrètement ?

Le frein culturel le plus visible chez NovaTech est le cloisonnement entre services (dimension Sharing de CALMS) : chaque équipe fonctionne comme une boîte noire pour les autres. C'est un fait, pas une hypothèse : l'exploitante "découvre certaines modifications la veille de la mise en production" (03_Incident_fictif.md), et la sécurité ne sait "pas toujours qui valide les exceptions" (01_Contexte_et_temoignages.md). Ce manque de partage empêche aussi la Mesure : sans visibilité commune, la direction elle-même ne sait pas si le problème vient des outils, des process ou de la collaboration.

Un second frein, lié au premier, est un manque de confiance entre équipes : il se traduit par une multiplication des validations manuelles à chaque étape (36h d'attente sur la seule validation des changements, voir 02_Processus_actuel.csv), plutôt que par des contrôles automatisés partagés. C'est l'inverse d'une culture Lean : on ralentit la livraison pour compenser un déficit de confiance, au lieu d'outiller la confiance (tests automatisés, critères écrits).

Comment l'observer concrètement : mesurer le délai entre la décision d'un changement et sa communication aux équipes concernées ; vérifier s'il existe un document écrit désignant un responsable des exceptions de sécurité, compter la part des validations qui reposent sur un jugement humain informel plutôt que sur des critères documentés.

- **Q4.4** - Qu'est-ce que la sécurité psychologique, et pourquoi conditionne-t-elle l'apprentissage après un incident ?

La sécurité psychologique est la conviction partagée par les membres d'une équipe qu'ils peuvent prendre des risques interpersonnels sans craindre de retombées négatives pour leur image, leur statut ou leur carrière. Concept popularisé par Amy Edmondson, professeure à la Harvard Business School, elle désigne un climat de confiance où l'on peut poser des questions, admettre une erreur, proposer une idée ou exprimer un désaccord sans peur d'être humilié ou blâmé.

Elle conditionne entière l’apprentissage après un incident car :

1. Elle permet de libérer la parole et de déclarer l'incident sans peur de représailles
2. Elle déplace le focus : On ne cherche plus sur qui rejeter la faute, on recherche plutôt la root cause
3. Elle favorise une analyse honnête et approfondie
4. Elle encourage l'expérimentation et l'innovation future sans peur.

Un incident est souvent le sous-produit d'une prise de risque ou d'une innovation qui a échoué. Si l'échec est puni, les équipes basculent dans une posture de sur-protection et de stagnation. La sécurité psychologique désamorce cette peur, transformant l'erreur en une source d'expérience précieuse permettant d'ajuster le tir pour les tentatives suivantes.

Source :

https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f

- **Q4.5** - Comment mesurer un changement culturel sans se limiter à un questionnaire de satisfaction ?

On ne demande pas aux gens s'ils se sentent plus en confiance, l’indicateur par ce simple questionnaire peux être biaiser par simple fait de vouloir bien se faire voir par sa hiérarchie, Le plan d’action à mettre en place serais de regarder si leurs actions montrent plus de “confiance”, par exemple est-ce que les équipes ont tendance à faire moins de double-validation ? Partage-t’il plus rapidement l'information ? Et on compare ça dans le temps, pas une seule fois par année ou par mois.

- **Q4.6** - ChatOps : dans quels cas une notification aide-t-elle l'équipe, et dans quels cas nuit-elle à son attention ?

Une notification ChatOps aide quand elle remplace une surveillance manuelle par une alerte rare et actionnable envoyée à la bonne personne ; elle nuit quand elle devient un flux constant d'informations non triées qui pousse l'équipe à moins y prêter attention, y compris aux alertes qui comptent.

- **Q4.7** - Comparez deux modèles d'organisation (équipe DevOps dédiée, équipes produit autonomes, Team Topologies, SRE…) et recommandez-en un pour NovaTech.

Plutôt que d'ajouter une équipe DevOps entre Dev et Ops, qui recréerait le cloisonnement déjà diagnostiqué, NovaTech devrait rapprocher Dev et Ops autour d'une responsabilité partagée du module de paiement, appuyée par des outils communs (la CI déjà en place), ce qui correspond à une version simplifiée du modèle d'équipe produit autonome plutôt qu'à une SRE complète, hors de portée d'une si petite structure.

Source :

https://teamtopologies.com/key-concepts

- **Q4.8** - Comment faire évoluer une culture sans l'imposer : quel rôle pour le leadership, et que faire si un acteur clé résiste ?

Le leadership fait évoluer la culture en donnant l'exemple, en finançant des essais réversibles et en traitant les résistances comme des signaux à comprendre plutôt que des obstacles à écraser. L'imposition par la contrainte ne reste qu'un dernier recours si la sécurité ou l'activité est directement en jeu.

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Les 5 dimensions CALMS et la collaboration

- **Culture :** les équipes se font confiance et partagent la responsabilité du résultat, au lieu de se renvoyer la balle.
- **Automation :** on laisse aux machines les tâches répétitives (tests, déploiements) pour éviter les oublis et gagner du temps.
- **Lean :** on travaille par petits morceaux et on enlève ce qui fait attendre sans apporter de valeur.
- **Measurement :** on mesure pour savoir si on s'améliore vraiment, au lieu de se fier à une impression.
- **Sharing :** on partage ce qu'on sait, ce qui marche et ce qui a raté, pour que tout le monde progresse.

Les cinq dimensions dépendent les unes des autres : sans culture de confiance, personne ne partage ses erreurs, et sans partage, impossible de mesurer quoi que ce soit de fiable. La collaboration n'est donc pas une lettre à part, elle traverse tout le modèle.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [DevOps Culture (Part 1)](https://itrevolution.com/articles/devops-culture-part-1/) | John Willis, IT Revolution | 21/10/2026 | John Willis et Damon Edwards ont créé l'acronyme CAMS (Culture, Automation, Measurement, Sharing) en 2010, après le premier DevOpsDays américain. Jez Humble a ensuite ajouté le L de Lean. | Source primaire : c'est l'un des auteurs du modèle qui le raconte. La date d'ajout du L n'est pas précisée. Publié le 01/05/2012. |
| [Principle-based DevOps frameworks: CALMS](https://www.sonatype.com/blog/principle-based-devops-frameworks-calms) | Ember DeBoer, Sonatype | 21/10/2026 | Définition de chaque lettre de CALMS. Le Lean y est décrit comme la limitation du travail en cours, la visibilité du travail et la réduction des attentes et des passages de relais. | Blog d'un éditeur de logiciels. Attribue tout le modèle à Jez Humble, ce qui contredit la source précédente. Publié le 23/09/2019. |
| [Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) | John Lunney et Sue Lueder, Google (livre *Site Reliability Engineering*) | 21/10/2026 | Un postmortem sans blâme cherche les causes d'un incident sans accuser une personne ou une équipe, en partant du principe que chacun a agi de bonne foi. Sans cela, les gens cachent les problèmes par peur d'être sanctionnés. | Retour d'expérience de Google, une très grande entreprise : à adapter à une structure comme NovaTech. Livre publié en 2017. |
| [Psychological Safety and Learning Behavior in Work Teams](https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f) | Amy Edmondson, *Administrative Science Quarterly* | 21/10/2026 | La sécurité psychologique est une croyance partagée que l'équipe est un lieu sûr pour prendre des risques interpersonnels. Sur 51 équipes étudiées, elle est liée au comportement d'apprentissage, qui est lui-même lié à la performance. | Article scientifique, source la plus solide du lot. Étude menée dans une seule entreprise industrielle, pas dans l'IT. Publié en 1999. |
| [Team Topologies - Key Concepts](https://teamtopologies.com/key-concepts) | Matthew Skelton et Manuel Pais | 21/10/2026 | Quatre types d'équipes (stream-aligned, enabling, complicated subsystem, platform) et trois modes d'interaction. Une équipe stream-aligned gère sa partie du produit de bout en bout (« You Built It, You Run It »), sans transfert vers une autre équipe. | Site des auteurs, qui vendent aussi formations et conseil. Ne parle pas des équipes DevOps dédiées. Pas de date de publication. |

## 4. Exemple professionnel commenté

Chez Google, chaque incident important donne lieu à un « postmortem » écrit, et la règle est claire : on ne cherche pas de coupable. Le document décrit ce qui s'est passé, l'impact, les causes et les actions à mener, en partant du principe que chacun a agi de bonne foi avec ce qu'il savait à ce moment-là. Les postmortems sont ensuite relus et partagés largement dans l'entreprise, pour que d'autres équipes en profitent.

Commentaire : Ce qui nous a marqué, c'est l'argument derrière : si on punit les erreurs, les gens finissent par les cacher, et l'entreprise n'apprend plus rien. On retrouve ici presque toutes les lettres de CALMS : la Culture (pas de blâme), le Sharing (les postmortems circulent) et la Mesure (on note l'impact). Chez NovaTech, la réunion improvisée du 16 octobre aurait pu servir de point de départ à ce type de revue, au lieu de rester une réunion de crise.

## 5. Expérimentation / analyse
**Piste :** Revue sans blâme, tableau Kanban, notification ChatOps fictive

- Hypothèse : Les problèmes de NovaTech sont d'abord culturels (cloisonnement, manque de confiance). Une revue d'incident sans blâme, des règles de travail écrites et une notification ChatOps bien conçue devraient rendre visibles des actions concrètes, là où une réunion de crise classique s'arrête à la recherche d'une cause.

- Protocole / méthode :
  1. Remplir la matrice CALMS : pour chaque lettre, un problème NovaTech, une action, un responsable et une mesure.
  2. Simuler une revue sans blâme de l'incident du 16 octobre à partir de `03_Incident_fictif.md`, en séparant les faits des hypothèses.
  3. Écrire les règles du tableau Kanban de l'équipe.
  4. Analyser l'étape « Notification ChatOps simulée » de la CI fournie (`.github/workflows/ci.yml`).

- Résultat observé ou simulation :

  **Matrice CALMS appliquée à NovaTech**

  | Dimension | Fait ou hypothèse NovaTech | Action | Responsable | Mesure |
  |---|---|---|---|---|
  | Culture | Fait : réunion de crise improvisée le 16/10, sans revue derrière | Revue sans blâme après chaque incident | Responsable de l'exploitation | Nombre d'actions issues des revues et réellement terminées |
  | Automation | Hypothèse : procédure de retour arrière manuelle, pas accessible le jour de l'incident | Retour arrière automatisé et testé dans le pipeline | Développeurs | Temps de restauration (95 min le 16/10) |
  | Lean | Fait : 36 h d'attente avant validation pour 1 h de travail | Validation quotidienne des petits changements (PDCA du module 2) | Responsable métier | Attente avant validation, en heures |
  | Measurement | Fait : la direction ne sait pas si le problème vient des outils, des processus ou de la collaboration | Tableau de bord avec les 5 métriques DORA | Product Owner | Mise à jour du tableau chaque semaine |
  | Sharing | Fait : l'Ops découvre des changements la veille, la sécurité ne sait pas qui valide les exceptions | Calendrier des changements partagé et responsable des exceptions écrit noir sur blanc | Responsable sécurité | Part des changements annoncés à l'Ops au moins 2 jours avant |

  **Revue sans blâme de l'incident du 16 octobre (simulation)**
  - Faits : déploiement à 16h45 un vendredi, premières erreurs à 16h52, réunion Dev/Ops à 17h05, procédure de retour arrière pas accessible tout de suite, service rétabli à 18h20 (95 min).
  - Impact : erreurs côté utilisateurs sur le module de paiement. Le nombre de clients touchés et l'impact financier ne sont pas connus.
  - Hypothèses : changement arrivé tard chez l'Ops, procédure de retour arrière pas tenue à jour, déploiement en fin de semaine avec moins de monde disponible. Aucune n'est prouvée.
  - Questions posées : « qu'est-ce qui a rendu la procédure difficile à trouver ? » plutôt que « qui ne l'a pas mise à jour ? ».
  - Actions : rendre la procédure de retour arrière accessible et la tester (Ops), annoncer les changements au moins 2 jours avant (Dev), récupérer les logs et métriques manquants avant de conclure sur la cause (Ops et Dev).

  **Règles du tableau Kanban**
  - Colonnes : À faire, En cours, En revue, Terminé.
  - Limite de WIP : 2 cartes par personne dans « En cours ».
  - Règle de revue : une carte ne passe en « Terminé » qu'après la relecture de la PR par un autre membre (le PO du jour, d'après `docs/review_policy.md`).
  - Définition de « Terminé » : PR fusionnée, CI au vert, issue fermée.

  **Analyse de la notification ChatOps de la CI**
  - Ce qu'elle fait : en cas d'échec des tests, elle écrit un résumé dans le run GitHub (branche, commit, lien vers le run, action attendue : « l'auteur du commit corrige ou annule le changement »).
  - Ce qui est utile : elle ne s'affiche qu'en cas d'échec, donc pas de bruit, et elle dit qui doit agir.
  - Ce qui manque : elle n'est envoyée dans aucun canal, donc personne n'est prévenu s'il ne va pas voir le run. Elle ne dit pas quel test a échoué.
  - Sécurité et confidentialité : en passant à un vrai canal, il ne faudrait jamais y copier de logs bruts ou de secrets. La recherche de secrets (job gitleaks) protège le dépôt, pas les messages envoyés dans le canal.

- Ce que ce résultat ne prouve pas : La revue d'incident est simulée sur un incident fictif, sans logs ni métriques : on ne connaît toujours pas la cause réelle. La matrice CALMS donne des pistes, mais rien ne prouve que ces actions changeraient la culture de NovaTech, ni que les responsables proposés seraient d'accord. La notification ChatOps a été analysée en lisant le fichier de CI, pas observée en échec (ce sera fait au module 5). Enfin, on n'a aucune mesure de la culture actuelle de NovaTech à comparer.

## 6. Application à NovaTech
- Problème visé : Les équipes de NovaTech travaillent en silo : l'Ops découvre les changements la veille, la sécurité ne sait pas qui valide les exceptions, et après l'incident du 16 octobre il n'y a eu qu'une réunion de crise, sans retour d'expérience.

- Action envisagée : Mettre en place une revue sans blâme après chaque incident, avec un format court et toujours le même (faits, impact, hypothèses, actions avec un responsable), et la partager avec toutes les équipes. Le management y participe sans chercher de coupable, pour montrer l'exemple.

- Indicateur et risque :

    - Indicateurs : le nombre d'incidents qui ont eu une revue, la part des actions décidées qui sont réellement terminées, et le temps de restauration (95 min le 16/10).

    - Risques : la revue peut tourner à la recherche de coupable si le management ne joue pas le jeu. Les actions peuvent aussi être décidées puis oubliées. Enfin, partager les revues peut exposer des informations sensibles sur le module de paiement : il faut faire attention à ce qui est diffusé.

## 7. Preuves déposées
**Attendu :** Matrice CALMS et note culture/sécurité
- Liens commits / MR / CI / fichiers :
  - Matrice CALMS dans la section 5 de ce fichier (à reporter dans `novatech/analyse-calms.md`) ;
  - `experiences/retour-incident.md` : à créer à partir de la revue simulée de la section 5 ;
  - `experiences/chatops.md` : à créer à partir de l'analyse de la section 5 ;
  - `.github/workflows/ci.yml` : étape « Notification ChatOps simulée ».

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a été utilisée pour mettre en forme le fichier, trouver et vérifier les sources (auteur, date, ce que dit réellement la page), et rédiger un premier jet des sections 2, 4, 5 et 6. L'analyse de la notification ChatOps a été faite à partir du vrai fichier de CI du dépôt.

## 10. Questions ouvertes / blocages

- Qui a réellement inventé CALMS ? Les sources ne sont pas d'accord : John Willis dit avoir créé CAMS avec Damon Edwards, alors que Sonatype attribue tout à Jez Humble. On a retenu la version de John Willis, qui est une source primaire.
- La notification ChatOps reste à observer en échec dans la CI (module 5).
