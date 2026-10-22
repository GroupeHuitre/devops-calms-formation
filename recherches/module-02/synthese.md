# Module 02 - Three Ways, contraintes, VSM, Kanban, PDCA

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q2.1 à Q2.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q2.1** - Quelles sont les trois voies de Gene Kim ? Expliquez chacune en une phrase avec un exemple.

Voici les trois voies de Gene Kim (Three Ways) citées dans le roman “The Phoenix Project”, lui-même basée sur le roman “The Goal” d’Eliyahu Goldratt. “The Phoenix Project” est une adaptation IT de “The Goal” qui lui est plus tourné vers l’organisation de la ligne de production industrielle. Les principes restent transcendants dans ces deux contextes, et au-delà.

**Flow :** Fluidifier la livraison  de valeur vite et sans blocage, du développeur jusqu'au client. Par exemple, livrer de petites modifications souvent, plutôt qu'un gros paquet de changement de temps en temps.

**Feedback :** Savoir très vite quand quelque chose ne va pas. Par exemple, réaliser des tests automatiques pour prévenir le développeur d'une éventuelle erreur avant que le client ne la découvre. Le but est d’avoir un signal permettant un retour d’expérience, et une amélioration incrémentale.

**Apprentissage continu :** Tirer des leçons de ses erreurs et essayer de s'améliorer en permanence. Par exemple, après une panne, l'équipe en analyse les causes sans chercher de coupable et teste une amélioration, dans une philosophie d’amélioration continue et incrémentale similaire à la ligne de production Toyota.

Sources :

https://itrevolution.com/articles/the-three-ways-principles-underpinning-devops/
https://itrevolution.com/articles/three-ways-revisited-devops-handbook/

- **Q2.2** - Qu'est-ce qu'un goulot d'étranglement, et qu'est-ce qu'une limite de travail en cours (WIP) ?

Le goulot d'étranglement est l'étape la plus lente d'un processus, celle qui ralentit tout le reste du projet. C’est également l’étape présentant le potentiel d’amélioration majeur du flux de travail. Il peut être humain (théorie des contraintes), lié à un manque de feedback et monitoring, ou par des outils et processus inadaptés.

La limite de WIP (Work In Progress) est le nombre maximum de tâches qu'une équipe peut avoir en cours et en même temps. Pour commencer une nouvelle tâche on doit finir une tâche en cours avant. Par exemple, "pas plus de trois cartes à la fois dans la colonne “En cours” du tableau Kanban". Il peut aussi s’agire d’un poids trop élever avec une priorité mal jaugée, qui aurais peut-être dû être ce qu’on appelle une “epic” (une vaste initiative ou un grand objectif stratégique que l'on découpe en éléments plus petits et gérables.). Il est nécessaire de hiérarchiser les tâches, les découper en taille viable pour une intégration continue et de définir la masse de travail acceptable.

Source :

https://kanbanguides.org/the-kanban-guide/2025.5/

- **Q2.3** - À partir de `02_Processus_actuel.csv`, calculez le temps actif, l'attente, le délai total et la part d'attente. Que révèlent ces chiffres ?

- Temps actif : 2+12+2+3+1+2 = 22h
- Temps d'attente : 6+4+10+24+36+8 = 88h
- Délai total : 22+88 = 110h
- Part d'attente : 88/110 = 80%

80% du temps, le "travail attend", il n'est exploité vraiment que 20% du temps. Le vrai problème est donc le temps d'attente entre les différentes étapes. Les plus longues attentes sont celles liées à la validation des changements (36h) et les tests (24h).

Ces chiffres rejoignent complètement le témoignage des développeurs : "Les validations et les déploiements prennent parfois plus de temps que le développement".

- **Q2.4** - Quelle différence faites-vous entre intégration continue, livraison continue et déploiement continu ?

Selon nous, ce sont trois niveaux d'automatisation, avec chacune son degré d'implication.

**CI (Intégration Continue) :** chaque modification du code est envoyée souvent sur le dépôt commun, puis testée automatiquement. Par exemple, à chaque push, le pipeline lance les tests et passe au rouge si une erreur est détectée.

**Continuous Delivery (Livraison Continue) :** en plus de la CI, le logiciel est toujours prêt à être mis en production, mais un humain décide tout de même quand on doit le déployer. Par exemple, la nouvelle version est prête, et le responsable clique sur "déployer" au moment voulu.

**Continuous Deployment (Déploiement Continu) :** chaque modification qui passe tous les tests part automatiquement en production, sans intervention humaine. Par exemple, un développeur corrige un bug, et quelques minutes plus tard la correction est en ligne pour les clients.

Sources :

https://martinfowler.com/bliki/ContinuousDelivery.html
https://martinfowler.com/articles/continuousIntegration.html

- **Q2.5** - La plus longue attente du processus est-elle forcément la contrainte du système ? Quelles données manquent pour le démontrer ?

Pas forcément. La contrainte est l'étape qui a le moins de capacité et qui limite donc le nombre de changements livrés. Chez NovaTech, la validation a la plus longue attente, mais cette attente peut venir d'une règle d'organisation, comme une validation par lots une fois par semaine, et non d'un manque de capacité. C'est donc une contrainte probable, pas une certitude.

Il nous manque comme détails :

- La capacité de chaque étape ;
- Le débit réel ;
- La quantité de travail en attente devant chaque étape ;
- Les règles de fonctionnement ;
- Plusieurs mesures dans le temps, et pas une seule valeur par étape.

- **Q2.6** - Pourquoi limiter le travail en cours peut-il réduire le délai de livraison alors que l'équipe démarre moins de tâches ? Appuyez-vous sur la loi de Little.

Voici ce que nous dit la loi de Little : délai = travail en cours / nombre de tâches terminée par semaine.

Moins de tâches simultanées, c'est moins d'attente pour chacune des tâches, donc des livraisons plus rapides. C’est également plus de ressources à déployer sur les tâches pour les livrer plus rapidement, et moins de temps à les hiérarchiser et prioriser.

Source :

https://www.infoq.com/articles/how-kanban-works

- **Q2.7** - Concevez une expérience PDCA ou Improvement Kata pour réduire l'attente avant validation : hypothèse, changement limité, mesure, critère d'arrêt.

Le PDCA (Plan, Do, Check, Act) est une boucle d'amélioration : on prévoit un changement, on le teste à petite échelle, on vérifie le résultat, puis on décide de la suite.

**Plan (prévoir)**

- Constat : l'attente avant validation est de 36 h pour 1 h de travail.
- Hypothèse : cette attente vient de la validation par lots. Si on valide les petit- changements chaque jour au lieu de les regrouper, l'attente baissera.
- Objectif : passer de 36 h à moins de 12 h d'attente.

**Do (tester à petite échelle)**

- Pendant 2 semaines, une courte réunion de validation de 15 minutes a lieu chaque jour.
- Seulement pour les changements à faible risque (pas le module de paiement).

**Check (vérifier)**

- Mesurer l'attente avant validation (en heures) pour chaque changement.
- Vérifier que le nombre d'incidents n'augmente pas.

**Act (décider)**

- Si l'attente passe sous 12 h sans plus d'incidents : on généralise.
- Critère d'arrêt : on arrête l'essai si un incident est causé par un changement validé de cette manière, ou si l'attente n'a pas baissé après 2 semaines.
- On fait un retour d’expérience et théorise de nouvelles informations à débattre au prochain daily

Source :

https://www.lean.org/lexicon-terms/pdca/

- **Q2.8** - Comment les trois voies se renforcent-elles ? Donnez un exemple où améliorer le Flow sans Feedback aggrave la situation.

Les trois voies fonctionnent ensemble :

- le Flow permet de livrer plus vite en fluidifiant la chaine de livraison de valeur ;
- le Feedback permet de voir rapidement si ce qu'on a livré pose problème et identifier les points de blocage et amélioration;
- L'apprentissage continu permet de tirer des leçons de ces retours pour s'améliorer par courts changements incrémentaux.

Chaque voie a besoin des autres et influencent les autres dans une boucle de rétroaction positive : livrer vite ne sert à rien si on ne sait pas si ça marche, et avoir des retours ne sert à rien si on n'en tire pas de leçons. Inversement, identifier les problèmes, proposer des améliorations incrémentales, analyse les résultats et recommencer permets de livrer de plus en plus vite.

Exemple : NovaTech décide de déployer beaucoup plus souvent (Flow) et de manière imprédictible (le nombre de déploiement varie par jours), mais sans tests automatiques ni surveillance de la production avant, pendant et après le déploiement (pas de Feedback). Le manque de données et monitoring ne permets pas de prendre des décisions impactantes, et l’absence d’environnement de test / staging ne favorise pas l’expérimentation et les tests pré déploiement en Production. Résultat : les erreurs arrivent plus vite et plus souvent, et c'est encore eux qui les découvrent, comme lors de l'incident du 16 octobre. Accélérer sans prédictibilité, monitoring, et feedback a donc aggravé la situation. Ils devraient prioriser des déploiements automatiques sous réserve de tests de validation, avec non-déploiement en cas d’erreur, afin d’éviter le temps extrêmement long de rollback.

Source :

https://itrevolution.com/articles/the-three-ways-principles-underpinning-devops/

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Flow, Feedback, Continual Learning & Experimentation

- **Flow :** faire avancer le travail du développeur jusqu'au client sans qu'il reste bloqué entre deux étapes. On regarde le flux en entier, pas seulement son équipe.
- **Feedback :** être prévenu le plus tôt possible quand quelque chose ne va pas, idéalement avant le client, pour corriger tant que c'est facile.
- **Continual Learning & Experimentation :** tester des petites améliorations, regarder si elles marchent, et apprendre des erreurs sans chercher de coupable.
- **Goulot d'étranglement / contrainte :** l'étape qui limite ce que tout le système peut livrer. Ce n'est pas forcément celle où on attend le plus longtemps.
- **WIP :** le nombre de tâches commencées mais pas finies. Le limiter évite de tout commencer et de ne rien finir.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [The Three Ways: The Principles Underpinning DevOps](https://itrevolution.com/articles/the-three-ways-principles-underpinning-devops/) | Gene Kim, IT Revolution | 21/10/2026 | Les trois voies : pensée systémique et Flow (optimiser tout le système et ne jamais passer un défaut connu à l'étape suivante), amplification des boucles de Feedback, culture d'expérimentation et d'apprentissage continu. | Source de l'auteur du concept, donc fiable pour la définition. L'article ne parle pas de *The Goal* : le lien avec Goldratt est à sourcer ailleurs. IT Revolution est aussi l'éditeur des livres de Gene Kim. Publié le 22/08/2012. |
| [The Three Ways Revisited (DevOps Handbook)](https://itrevolution.com/articles/three-ways-revisited-devops-handbook/) | IT Revolution | 21/10/2026 | *The DevOps Handbook* (Kim, Humble, Debois, Willis, puis Forsgren pour la 2e édition) est construit autour des trois voies : Flow, Feedback, apprentissage continu et expérimentation. | Article promotionnel de l'éditeur du livre. Publié le 30/11/2021. |
| [The Kanban Guide v2025.5](https://kanbanguides.org/the-kanban-guide/2025.5/) | Vacanti, Coleman et al. (Orderly Disruption Ltd, Daniel S. Vacanti Inc.) | 21/10/2026 | Le WIP est le nombre d'éléments commencés mais pas terminés. L'équipe doit le contrôler explicitement, ce qui crée un système « pull » où on ne démarre une tâche que si la capacité le permet. | Le guide ne donne aucune valeur de limite et ne parle pas de goulot d'étranglement. Version mise à jour le 01/05/2025. |
| [Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html) | Martin Fowler | 21/10/2026 | En livraison continue, le logiciel peut être mis en production à tout moment, mais l'équipe choisit quand. En déploiement continu, chaque changement validé part automatiquement en production. | Référence reconnue, mais c'est un article de blog. Publié le 30/05/2013, mis à jour le 12/08/2014. |
| [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) | Martin Fowler | 21/10/2026 | Chaque membre intègre ses changements dans la branche principale au moins une fois par jour, et chaque intégration est vérifiée par un build et des tests automatiques. | Article de référence, réécrit plusieurs fois (2000, 2006, révision publiée le 18/01/2024). |
| [How Kanban Works](https://www.infoq.com/articles/how-kanban-works) | Amr Noaman Abdel-Hamid, InfoQ | 21/10/2026 | Loi de Little : WIP = débit × temps de cycle, donc temps de cycle = WIP / débit. Au-delà de la capacité de l'équipe, augmenter le WIP fait baisser le débit (stress, changements de tâche). | Article de praticien (coach agile), pas une étude. Publié le 31/07/2014. |
| [PDCA](https://www.lean.org/lexicon-terms/pdca/) | Lean Enterprise Institute | 21/10/2026 | Le PDCA est un cycle d'amélioration basé sur la méthode scientifique : Plan, Do, Check, Act. Il vient du cycle de Shewhart, repris par Deming au Japon dans les années 1950. | Pas d'auteur ni de date de publication sur la page. |
| [Andon](https://www.lean.org/lexicon-terms/andon/) | Lean Enterprise Institute | 21/10/2026 | Chez Toyota, tout opérateur qui rencontre un problème tire une corde. L'équipe essaie de le régler pendant le cycle, et si ce n'est pas réglé à temps, la ligne s'arrête à une position fixe. | Pas d'auteur ni de date sur la page. Contexte industriel, à transposer avec prudence à l'IT. |

## 4. Exemple professionnel commenté

Chez Toyota, chaque opérateur de la ligne de production peut tirer une corde, appelée « andon », dès qu'il repère un problème. Un voyant s'allume, le chef d'équipe vient aider, et si le problème n'est pas réglé à temps, la ligne s'arrête. L'idée, c'est de ne jamais laisser passer un défaut à l'étape suivante, même si ça veut dire ralentir la production sur le moment.

Commentaire : On retrouve les trois voies dans ce seul geste. Le Feedback est immédiat, puisque le problème est signalé là où il apparaît. Le Flow est protégé, parce qu'un défaut corrigé tout de suite coûte bien moins cher qu'un défaut découvert à la fin. Et chaque arrêt est l'occasion de comprendre ce qui s'est passé. Pour nous, l'équivalent en IT, c'est un pipeline de CI qui passe au rouge et bloque la fusion : ça peut paraître frustrant, mais c'est toujours mieux que de découvrir le bug en production, comme NovaTech le 16 octobre.

## 5. Expérimentation / analyse
**Piste :** Données de processus + comparaison d’actions

- Hypothèse : Le délai de livraison de NovaTech vient surtout des attentes entre les étapes, et pas du temps de travail. Agir sur la plus longue attente (la validation) devrait donc réduire le délai total bien plus qu'une action sur une autre étape.

- Protocole / méthode : On a repris `02_Processus_actuel.csv` et calculé, pour chaque étape, le temps actif et l'attente, puis les totaux. On a ensuite simulé trois actions possibles, en changeant une seule valeur à la fois pour comparer leur effet sur le délai total :
  - A : validation quotidienne au lieu de par lots (attente de validation 36 h → 12 h, l'objectif de notre PDCA en Q2.7) ;
  - B : environnement de test partagé (attente des tests 24 h → 8 h) ;
  - C : reviewers désignés chaque jour (attente de revue 10 h → 4 h).

  Les valeurs « après » sont nos hypothèses, pas des mesures.

- Résultat observé ou simulation :

  | Étape | Actif (h) | Attente (h) |
  |---|---:|---:|
  | Spécification | 2 | 6 |
  | Développement | 12 | 4 |
  | Revue de code | 2 | 10 |
  | Tests | 3 | 24 |
  | Validation changement | 1 | 36 |
  | Déploiement | 2 | 8 |
  | **Total** | **22** | **88** |

  Situation actuelle : délai total de 110 h, dont 80 % d'attente.

  | Action simulée | Attente gagnée | Délai total | Part d'attente |
  |---|---:|---:|---:|
  | Aucune (actuel) | 0 h | 110 h | 80 % |
  | A - Validation quotidienne | 24 h | 86 h | 74 % |
  | B - Environnement de test partagé | 16 h | 94 h | 77 % |
  | C - Reviewers désignés | 6 h | 104 h | 79 % |
  | A + B + C | 46 h | 64 h | 66 % |

  Dans ce modèle, l'action A est celle qui fait gagner le plus de temps. Même en combinant les trois actions, l'attente reste majoritaire (66 %), donc il reste de la marge sur les autres étapes.

- Ce que ce résultat ne prouve pas : Les valeurs après action sont des objectifs qu'on a fixés, pas des résultats mesurés. Le modèle additionne simplement les durées : il ne tient pas compte du travail en parallèle, de la variabilité, de la capacité des équipes ni du nombre de changements en file. On ne peut donc pas dire que la validation est la contrainte du système (voir Q2.5), seulement que c'est la plus longue attente. Enfin, les données sont fictives et donnent une seule valeur par étape, et rien ne dit qu'une validation plus rapide n'augmenterait pas le nombre d'incidents.

## 6. Application à NovaTech
- Problème visé : Les changements attendent 36 h avant d'être validés pour 1 h de travail réel, très probablement parce qu'ils sont validés par lots.

- Action envisagée : Lancer l'essai PDCA décrit en Q2.7 : une validation quotidienne de 15 minutes pendant 2 semaines, uniquement pour les changements à faible risque (pas le module de paiement). En parallèle, suivre le travail sur un tableau Kanban (À faire, En cours, En revue, Terminé) avec une limite de WIP sur la colonne « En revue ».

- Indicateur et risque :

    - Indicateurs : l'attente avant validation en heures (actuellement 36 h, objectif sous 12 h), le délai total du processus (110 h actuellement) et le nombre d'incidents causés par les changements validés pendant l'essai.

    - Risques : une validation plus rapide peut devenir moins sérieuse et laisser passer des erreurs. La réunion quotidienne peut aussi être sautée quand l'équipe est chargée, et l'attente reviendrait. Enfin, l'attente peut simplement se déplacer vers le déploiement (8 h aujourd'hui) si la fenêtre de mise en production ne change pas.

## 7. Preuves déposées
**Attendu :** Schéma de flux et mesure des attentes
- Liens commits / MR / CI / fichiers :
  - `docs/bottleneck_analysis.md` : goulots par domaine et tableau VSM ;
  - `novatech/value-stream-map.md` : à compléter avec les chiffres de la section 5 ;
  - Issue d'expérimentation PDCA : à créer ;
  - Lien ou capture du tableau Kanban : à ajouter.

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a été utilisée pour mettre en forme le fichier, vérifier les sources citées (auteur, date, ce que dit réellement la page) et rédiger un premier jet des sections 2, 4, 5 et 6. Les calculs ont été refaits à partir de `02_Processus_actuel.csv`, et les valeurs « après action » de la section 5 sont des hypothèses de l'équipe.

## 10. Questions ouvertes / blocages

- Quelle est la capacité réelle de chaque étape (nombre de changements traités par jour) ? Sans elle, on ne peut pas confirmer la contrainte.
- Pourquoi la validation se fait-elle par lots : règle de la direction, manque de disponibilité, contrainte réglementaire ?
