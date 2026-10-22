# Expérience - Revue d'incident sans blâme (TP3)

## Hypothèse
Une revue structurée qui sépare faits, impact, hypothèses et actions (plutôt que de chercher un responsable) permet de produire des actions d'amélioration concrètes même avec un dossier incomplet, et sans braquer les équipes concernées.

## Prérequis
`donnees-novatech/03_Incident_fictif.md` (chronologie et pièces manquantes de l'incident fictif du 16/10/2026).

## Démarche
Faute de temps pour réunir les 4 membres en vrai, la réunion a été rejouée sous forme de scénario écrit, en s'appuyant sur les témoignages de `01_Contexte_et_temoignages.md` et la chronologie de `03_Incident_fictif.md` pour garder des positions réalistes. Format : faits → impact → hypothèses (non blâmantes) → actions avec propriétaire.

### Transcription du scénario rejoué

**Facilitateur :** On est réunis suite à l'incident du 16 octobre. Rappel rapide avant de commencer : on cherche à comprendre ce qui s'est passé dans le système, pas qui a fait une erreur. Si quelqu'un se sent visé à un moment, on arrête et on reformule.

**Métier :** Moi ce qui m'inquiète surtout c'est qu'on n'a toujours pas de chiffre. 95 minutes de paiement cassé un vendredi après-midi, ça peut vouloir dire beaucoup de clients qui abandonnent leur panier. On a une estimation ?

**Dev :** Non, pas pour l'instant. Et honnêtement je pense pas qu'on l'aura facilement, on n'a pas les logs ni les métriques de la période. Ce que je peux dire c'est que le changement avait été testé avant d'être livré, mais je ne sais pas avec certitude si le scénario qui a planté faisait partie des cas couverts par les tests.

**Ops :** C'est un peu ça le problème en fait. Moi j'ai appris qu'il y avait un changement sur le paiement la veille au soir, et là le vendredi ça part en prod à 16h45. Je n'ai pas eu le temps de vérifier qu'on avait un plan de retour arrière prêt pour ce cas précis. Du coup quand les erreurs sont arrivées à 16h52 j'ai dû chercher la procédure en live, pendant que ça continuait à planter pour les clients.

**Facilitateur :** Donc entre la découverte du changement et la mise en prod, il y avait moins de 24h pour se préparer côté Ops, c'est ça ?

**Ops :** Oui à peu près.

**Sécurité :** De mon côté j'avais fait une revue, mais elle portait sur une version antérieure du changement je crois. Il y a eu une petite modif après mon contrôle, et je ne suis pas certain qu'elle soit repassée par moi ou que quelqu'un d'autre ait validé l'exception. C'est flou, et ça devrait pas l'être.

**Métier :** Donc si je comprends bien, personne n'a vraiment eu le temps de faire son travail correctement avant que ça parte en prod.

**Dev :** C'est un peu dur dit comme ça, mais oui, la fenêtre entre "c'est prêt côté dev" et "c'est en prod" était trop courte pour que tout le monde fasse sa part sereinement.

**Facilitateur :** OK, on reste sur le système alors. On a trois pistes qui reviennent : le retour arrière pas prêt, la revue sécurité pas forcément à jour sur la dernière version, et le fait que personne d'autre que le dev ne savait précisément ce qui partait en prod avant que ça parte. On garde ça comme hypothèses, pas comme causes prouvées, vu qu'on n'a ni logs ni résultat de tests sous la main.

**Ops :** Ce que je voudrais vraiment, c'est qu'on ait une procédure de rollback écrite et testée pour le module de paiement. Pas juste "on sait le faire en théorie".

**Sécurité :** Et moi je veux juste qu'on sache clairement qui valide une exception si le code change après ma revue. Même une règle simple, mais écrite.

**Métier :** Et moi j'aimerais être prévenue plus tôt des changements sur le paiement, pas forcément pour bloquer, juste pour ne pas être surprise si ça part mal pendant une période commerciale importante.

**Facilitateur :** Ça fait des actions concrètes. On les note et on se revoit dans 30 jours pour voir si ça a bougé.

### Faits établis (chronologie)
| Heure | Fait |
|---|---|
| 16h45 | Mise en production d'une évolution du module de paiement |
| 16h52 | Premières erreurs utilisateurs signalées |
| 17h05 | Réunion improvisée Dev/Ops ; procédure de retour arrière non immédiatement accessible |
| 18h20 | Service rétabli (95 minutes après le déploiement) |

### Impact
- Service de paiement indisponible ou dégradé pendant 95 minutes.
- Impact financier et nombre de clients touchés : **non chiffrables** avec les données disponibles (information manquante, cf. `03_Incident_fictif.md`).
- Détection par signalement client (16h52) plutôt que par une alerte automatique, pas de preuve de monitoring proactif.

### Hypothèses (formulées sur le système, pas sur une personne)
1. L'absence de procédure de retour arrière *testée et documentée* a probablement allongé le délai de rétablissement (fait partiel : la procédure n'était « pas immédiatement accessible », cause de l'allongement non prouvée formellement).
2. Le processus de validation par lots (hypothèse du module 2) a pu empêcher une détection plus précoce du problème avant mise en production.
3. L'absence de monitoring automatique déclenchant une alerte avant le signalement client suggère un déficit d'observabilité.
4. Aucune des trois hypothèses n'est confirmée : les logs applicatifs, le résultat des tests avant déploiement et l'identifiant exact du changement manquent (cf. « pièces manquantes » du dossier).

### Actions proposées (avec propriétaire provisoire)
| Action | Propriétaire proposé | Indicateur de suivi |
|---|---|---|
| Documenter et tester une procédure de retour arrière pour le module de paiement | Équipe Ops + Dev conjointement | Temps de retour arrière mesuré lors du prochain exercice |
| Mettre en place une alerte automatique de santé (health check) avant mise en production | Équipe Ops | Délai détection automatique vs signalement client |
| Étudier le passage d'une validation par lots à une validation continue pour les changements à faible risque | Coordination du jour (module 2/4) | Attente moyenne à l'étape « Validation changement » |
| Clarifier par écrit qui valide les exceptions de sécurité | Responsable sécurité | Existence d'un document nommé et daté |

## Résultat observé ou simulation
**Simulé, pas joué en direct.** Faute de temps pour une vraie session à 4, le scénario ci-dessus a été rédigé à l'avance pour représenter une réunion plausible, en se basant sur les positions réelles de chaque fonction dans `01_Contexte_et_temoignages.md`. Ce n'est pas le compte-rendu d'une réunion qui a eu lieu.

## Preuve
`donnees-novatech/03_Incident_fictif.md` et `01_Contexte_et_temoignages.md` (sources utilisées pour construire le scénario).

## Limites
- Incident fictif, sans logs ni métriques réelles : toute cause reste une hypothèse, jamais une certitude.
- Le scénario est écrit, pas joué par l'équipe : on ne sait pas si une vraie discussion à 4 suivrait le même déroulé ni si le ton « sans blâme » tiendrait aussi facilement en vrai.
- Les propriétaires d'action sont par fonction (Dev, Ops, Sécurité, Métier), pas par personne réelle de l'équipe tant que les rôles ne sont pas attribués.

## Prochaine action
Si le temps le permet, relire ce scénario à 4 en 5 minutes et dire s'il sonne juste ou pas, pour pouvoir le présenter comme validé par l'équipe plutôt que comme un texte uniquement écrit en amont.
