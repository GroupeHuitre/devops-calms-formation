# Module 07 - DORA, fiabilité, observabilité, amélioration

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 22/10/2026

## 1. Questions traitées
Questions Q7.1 à Q7.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q7.1** - Quelles sont les cinq métriques DORA actuelles ? Définissez chacune en une phrase.

- **Fréquence de déploiement :** combien de fois on met en production sur une période donnée.
- **Change lead time :** le temps entre le moment où un changement est enregistré dans Git et celui où il arrive en production.
- **Change fail rate :** la part des déploiements qui ont causé un problème et demandé une intervention immédiate (retour arrière, correctif d'urgence).
- **Failed deployment recovery time :** le temps qu'il faut pour rétablir le service après un déploiement raté.
- **Deployment rework rate :** la part des déploiements qui n'étaient pas prévus et qui ont été faits pour corriger un incident en production.

Les deux premières mesurent la vitesse, les trois autres la stabilité.

Source : https://dora.dev/guides/dora-metrics/

- **Q7.2** - Quelle différence faites-vous entre logs, métriques et traces ?

- **Logs :** des messages écrits par l'application, avec la date et l'heure (« démarrage », « erreur de paiement »…). Utiles pour comprendre ce qui s'est passé à un moment précis.
- **Métriques :** des chiffres regroupés dans le temps (nombre d'erreurs par minute, temps de réponse, utilisation du processeur). Utiles pour voir une tendance ou déclencher une alerte.
- **Traces :** le chemin complet d'une requête à travers les différents services. Utiles pour savoir où une requête a ralenti ou échoué.

En gros : la métrique dit qu'il y a un problème, la trace dit où, et le log dit ce qui s'est passé.

Source : https://opentelemetry.io/docs/concepts/observability-primer/

- **Q7.3** - Calculez les cinq métriques sur `04_Deploiements_fictifs.csv` en donnant le numérateur, le dénominateur, l'unité et la période.

Période : du 20/09/2026 au 19/10/2026, soit 30 jours, avec 20 déploiements.

| Métrique | Numérateur | Dénominateur | Résultat | Unité |
|---|---|---|---|---|
| Fréquence de déploiement | 20 déploiements | 30 jours | 20 par 30 jours (≈ 0,67 par jour) | déploiements / période |
| Change lead time | somme des 20 délais : 1 102 h | 20 déploiements | moyenne 55,1 h, médiane 55 h | heures |
| Change fail rate | 3 déploiements défaillants (D04, D11, D17) | 20 déploiements | 15 % | % |
| Deployment rework rate | 2 déploiements de correction (D05, D18) | 20 déploiements | 10 % | % |
| Failed deployment recovery time | 130 + 75 + 95 = 300 min | 3 déploiements défaillants | moyenne 100 min, médiane 95 min | minutes |

Le lead time de chaque déploiement est calculé comme `deployed_at - committed_at`. Il va de 14 h (D18) à 96 h (D01 et D11).

- **Q7.4** - Pourquoi la médiane du délai de livraison peut-elle être plus parlante que la moyenne ?

Parce que la moyenne se fait tirer par les valeurs extrêmes. Si un changement reste bloqué deux semaines, la moyenne grimpe d'un coup, alors que la plupart des changements passent normalement. La médiane, elle, donne la valeur du milieu : la moitié des changements est plus rapide, l'autre moitié plus lente. Elle représente mieux un changement « typique ».

Dans nos données, les deux sont presque égales (55,1 h et 55 h), car il n'y a pas de valeur vraiment extrême. Mais c'est justement en comparant les deux qu'on repère quand quelques cas anormaux faussent le chiffre.

- **Q7.5** - Pourquoi le temps de restauration DORA n'est-il pas le MTTR de toutes les pannes ?

Parce que la métrique DORA ne mesure que le temps de rétablissement après un **déploiement raté**. Le MTTR (temps moyen de réparation) compte toutes les pannes, quelle que soit leur cause : un serveur qui tombe, un fournisseur cloud en panne, une attaque…

Une équipe peut donc avoir un très bon temps de restauration DORA et quand même subir de longues pannes qui n'ont rien à voir avec ses déploiements.

Source : https://dora.dev/guides/dora-metrics/

- **Q7.6** - Quelles conclusions ne peut-on pas tirer de ces données fictives ? Citez au moins trois limites.

1. **Les données sont fictives :** elles servent à s'entraîner au calcul, pas à juger la vraie performance de NovaTech.
2. **Une seule période de 30 jours :** impossible de savoir si NovaTech s'améliore ou se dégrade, il faudrait comparer plusieurs périodes.
3. **Un échantillon très petit :** 3 déploiements défaillants seulement. Un seul échec de plus ou de moins ferait passer le taux d'échec de 15 % à 20 % ou 10 %.
4. **Un seul commit par déploiement :** en réalité, un déploiement contient souvent plusieurs commits, donc le vrai lead time serait différent.
5. **Aucune cause :** les chiffres disent combien de déploiements ont échoué, pas pourquoi. Ils ne prouvent pas non plus que nos propositions amélioreraient quoi que ce soit.

- **Q7.7** - Comment éviter qu'une métrique devienne un objectif manipulable (loi de Goodhart) ? Proposez des garde-fous.

La loi de Goodhart dit que quand une mesure devient un objectif, elle cesse d'être une bonne mesure. Par exemple, si on exige « un déploiement par jour », une équipe peut découper artificiellement ses changements pour atteindre le chiffre, sans rien améliorer.

Quelques garde-fous :
- **Regarder les métriques ensemble :** vitesse et stabilité. Déployer plus souvent ne compte que si le taux d'échec ne monte pas.
- **Ne pas en faire des objectifs individuels**, ni les lier à des primes.
- **Comparer une équipe à elle-même dans le temps**, pas les équipes entre elles.
- **Discuter des chiffres en équipe**, pour comprendre ce qu'il y a derrière, plutôt que de juger sur un chiffre seul.

Source : https://dora.dev/guides/dora-metrics/

- **Q7.8** - Concevez un tableau de bord combinant DORA, indicateurs métier et observabilité pour NovaTech : quelles décisions permettrait-il de prendre ?

Un tableau de bord en trois parties, partagé par toutes les équipes et la direction :

| Partie | Indicateurs | Qui le regarde |
|---|---|---|
| **Livraison (DORA)** | Les 5 métriques DORA, suivies chaque semaine | Dev, Ops, direction |
| **Métier** | Taux de paiements réussis, commandes abandonnées, évolutions livrées à temps pour les campagnes | Responsable métier, direction |
| **Observabilité** | Taux d'erreur et temps de réponse du module de paiement, disponibilité du site, alertes en cours | Ops, Dev |

Les décisions qu'il permettrait de prendre :
- **Déployer ou attendre :** si le taux d'erreur du paiement monte, on gèle les nouveaux déploiements et on stabilise d'abord.
- **Où investir :** si le taux d'échec reste haut, on met la priorité sur les tests et le retour arrière plutôt que sur de nouvelles fonctionnalités.
- **Est-ce que nos essais marchent :** par exemple, vérifier que la validation quotidienne réduit bien le lead time sans augmenter les incidents.
- **Répondre au métier :** montrer avec des chiffres quand une évolution sera vraiment disponible pour une campagne.

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Cinq métriques DORA actuelles, PDCA

- **Les métriques DORA :** cinq chiffres pour savoir si on livre vite (fréquence, lead time) et si on livre bien (échecs, temps de rétablissement, déploiements de correction). Il faut toujours les regarder ensemble.
- **L'observabilité :** être capable de comprendre ce qui se passe dans l'application grâce aux logs, aux métriques et aux traces, surtout quand quelque chose casse.
- **Le PDCA :** une boucle pour s'améliorer petit à petit. On prévoit un changement, on le teste en petit, on mesure, puis on décide de le garder ou non.
- **La loi de Goodhart :** dès qu'un chiffre devient un objectif, les gens trouvent des moyens de l'atteindre sans vraiment s'améliorer.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) | DORA (Google Cloud) | 22/10/2026 | Les cinq métriques actuelles, réparties entre débit et instabilité. Mises en garde : ne pas en faire des objectifs (loi de Goodhart), ne pas comparer les équipes entre elles, ne pas regarder une métrique seule. | Source de référence sur le sujet, mais publiée par Google. Mise à jour le 05/01/2026. |
| [Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) | OpenTelemetry (CNCF) | 22/10/2026 | Définitions des logs, des métriques et des traces, et de l'observabilité. | Documentation d'un projet open source. Pas de date. |
| [Embracing Risk](https://sre.google/sre-book/embracing-risk/) | Marc Alvidrez et Mark Roth, Google (livre *Site Reliability Engineering*) | 22/10/2026 | Chez Google, un objectif de disponibilité (SLO) fixe un « budget d'erreur ». Tant qu'il reste du budget, on déploie. Quand il est épuisé, les mises en production sont suspendues et l'équipe travaille sur la fiabilité. | Pratique d'une très grande entreprise, à adapter à une structure comme NovaTech. Livre publié en 2017. |
| `donnees-novatech/04_Deploiements_fictifs.csv` et `05_Notice_des_donnees.md` | Dossier NovaTech (fictif) | 22/10/2026 | 20 déploiements sur 30 jours, 3 défaillants, 2 de correction, 3 durées de restauration. | Données fictives, simplifiées pour l'exercice. |

## 4. Exemple professionnel commenté

Chez Google, les équipes produit et les équipes de fiabilité (SRE) se mettent d'accord sur un objectif de disponibilité, par exemple 99,9 % sur un trimestre. Ce qui reste entre la disponibilité réelle et cet objectif devient un « budget d'erreur ». Tant que le budget n'est pas épuisé, les équipes peuvent déployer autant qu'elles veulent. S'il est épuisé, les nouvelles mises en production sont mises en pause et tout le monde travaille sur la stabilité.

Commentaire : Ce qui nous plaît dans cet exemple, c'est que la mesure sert à prendre une décision, pas à juger les équipes. Le chiffre est le même pour tout le monde, donc il n'y a plus de dispute entre « on veut livrer » et « on veut de la stabilité » : c'est le budget qui tranche. Chez NovaTech, ça pourrait remplacer le conflit entre le métier, qui veut ses évolutions à temps, et l'Ops, qui veut éviter les incidents.

## 5. Expérimentation / analyse
**Piste :** Calcul des données fictives, scénario PDCA

- Hypothèse : Les données de déploiement de NovaTech montrent des livraisons assez fréquentes, mais un délai long entre le commit et la mise en production. L'essentiel de ce délai viendrait de l'attente (validation par lots), pas du travail lui-même.

- Protocole / méthode : On a calculé les cinq métriques DORA à partir de `04_Deploiements_fictifs.csv`, en suivant les définitions de la notice des données (voir Q7.3). On a ensuite comparé avec le processus du module 2 (`02_Processus_actuel.csv`), puis construit une boucle PDCA pour tester une amélioration.

- Résultat observé ou simulation :

  - Fréquence : 20 déploiements en 30 jours, donc NovaTech déploie déjà assez souvent.
  - Lead time : 55 h en médiane, soit plus de 2 jours entre un commit et sa mise en production.
  - Stabilité : 15 % des déploiements ont échoué, et il a fallu en moyenne 100 min pour rétablir le service.
  - Lien avec le module 2 : 80 % du délai total du processus est de l'attente, dont 36 h pour la seule validation des changements.

  **Boucle PDCA proposée**

  | Étape | Contenu |
  |---|---|
  | **Plan** | Hypothèse : le lead time est long à cause de la validation par lots. Objectif : passer d'une médiane de 55 h à moins de 36 h. |
  | **Do** | Pendant 2 semaines, une validation quotidienne de 15 min pour les changements à faible risque (pas le module de paiement). |
  | **Check** | Recalculer le lead time médian et le change fail rate sur ces 2 semaines, avec la même méthode. |
  | **Act** | Si le lead time baisse sans hausse du taux d'échec, on généralise. Si le taux d'échec monte, on arrête et on cherche pourquoi. |

- Ce que ce résultat ne prouve pas : Les données sont fictives et couvrent une seule période de 30 jours, donc on ne voit aucune évolution. Le lien entre le lead time et la validation par lots est une hypothèse : le fichier de déploiements ne dit pas où le temps est perdu. Enfin, la boucle PDCA n'a pas été lancée : ses objectifs sont des cibles, pas des résultats.

## 6. Application à NovaTech
- Problème visé : La direction ne sait pas si le problème vient des outils, des processus ou de la collaboration, parce que personne ne mesure la livraison de façon commune.

- Action envisagée : Mettre en place le tableau de bord de la Q7.8, partagé par toutes les équipes : les 5 métriques DORA, quelques indicateurs métier (paiements réussis, évolutions livrées à temps) et l'observabilité du module de paiement. Il serait revu chaque semaine en équipe et chaque mois avec la direction.

- Indicateur et risque :

    - Indicateurs : le lead time médian (55 h aujourd'hui), le change fail rate (15 %) et le taux de paiements réussis (à mesurer, on n'a pas la valeur actuelle).

    - Risques : que les chiffres deviennent des objectifs à atteindre à tout prix, et que les équipes les manipulent (loi de Goodhart, Q7.7). Que le tableau de bord soit construit puis jamais regardé. Ou qu'on compare les équipes entre elles au lieu de suivre leur évolution.

## 7. Preuves déposées
**Attendu :** Tableau des indicateurs avec unités/limites
- Liens commits / MR / CI / fichiers :
  - Tableau des indicateurs avec unités et période : Q7.3 de ce fichier ;
  - Limites des données : Q7.6 de ce fichier ;
  - Données sources : `donnees-novatech/04_Deploiements_fictifs.csv` ;
  - Fichier de calcul avec les formules (TP 6) : à créer dans `novatech/`.

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a aidé à rédiger les réponses Q7.1 à Q7.8 et a vérifié chaque source (auteur, date, ce que dit réellement la page). Les calculs de la Q7.3 ont été faits à partir du fichier `04_Deploiements_fictifs.csv` et sont à revérifier par l'équipe.

## 10. Questions ouvertes / blocages

- Les calculs de la Q7.3 ont été faits à la main : il faut les recontrôler dans un tableur ou un script (TP 6).
- Quels indicateurs métier NovaTech mesure-t-elle déjà ? Le dossier ne le dit pas, il faudrait le demander au responsable métier.
