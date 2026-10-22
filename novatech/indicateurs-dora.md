# DORA — cinq mesures (données fictives)

Période observée : … jours. Source : `donnees-novatech/04_Deploiements_fictifs.csv`.
Fichier de calcul (tableur ou script, formules visibles) : `novatech/…`

| Métrique | Définition + numérateur/dénominateur | Calcul | Unité | Limites |
|---|---|---|---|---|
| Deployment frequency | nombre de déploiement par jours : 20déploiement/30jours | 20/30 = 0,67|déploiement/J| Période sur un mois, trop court il faudrait plusieurs mois pour voir si c'est constant ou non |
| Change lead time (moyenne, médiane) | 1102 heures/20déploiements | moyenne: 1102/20=55,1; médiane = 55  | heures | |
| Failed deployment recovery time | 75+95+130=300 300minutes/3déploiements_défaillant | moyenne: 300/3=100; médiane = 95  | minutes |  |
| Change fail rate | nombre d'incident par déploiement : changement_avec_incident/nombre_déploiement | 3/20=0,15 | incident/deploiement | l'échantillon est petit, il n'y ap as assez de déploiement, peut-être que ce mois il y a eu plus de défaillance ou moins que d'habitude |
| Deployment rework rate | nombre de rework par déploiement : changement_de_révision/nombre_déploiement | 2/20=0.1 | rework/deploiement | l'échantillon est petit, il n'y ap as assez de déploiement, peut-être que ce mois il y a eu plus de défaillance ou moins que d'habitude |

Autre limites : On a un manque de transparence sur les raisons de l'échec, on ne peut donc pas déterminer de bonnes solutions pour remédier à ce problème, on est obligé de faire des propositions à l'aveugle, c'est à dire les propositions basiques et non forcément les bonnes propositions pour l'entreprise.
## Interprétation : observations et hypothèses

Ce que l'on peut voir est un taux d'erreurs par changement élevé, il y a probablement un manque de commit, petites versions et de déploiement. afin de découper les problèmes. ça permettrait également de réduire le failed deployment recovery time, puisque les erreurs seraient plus petites, les développeurs pourraient également plus rapidement comprendre d'où provient l'erreur (actuellement les déploiements et les changements des développeurs ont plusieurs jours entre eux, ce qui veut dire qu'un développeur est passé sur une autre fonctionnalité et doit prendre du temps pour reprendre le contexte) 


## Quelle amélioration proposée, quelle mesure avant/après ?

Il faut réduire la taille des versions, voir si les change fail rate sont similaire ou si le taux baisse. De même pour le temps de récupération, normalement il devrait baissé, car les éléments à vérifier seront moindre et le développeur devrait toujours avoir le contexte (contrairement à si l'on fait un gros changement sur plusieurs fonctionnalités)

## Boucle PDCA envisagée
| Étape | Cotenu |
|---|---|
| Plan |  le lead time est long à cause de la validation par lots. Objectif : passer d'une médiane de 55 h à moins de 36 h. |
| Do  | Pendant 2 semaines, faire une validation quotidienne de 15 min pour les changements à faible risque |
| Act  | Recalculer le lead time médian et le change fail rate sur ces 2 semaines, avec la même méthode. |
| Check | Si le lead time baisse sans hausse du taux d'échec, on généralise. Si le taux d'échec monte, on arrête et on cherche pourquoi. |
