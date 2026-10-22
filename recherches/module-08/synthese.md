# Module 08 - Adoption DevOps en entreprise

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 22/10/2026

## 1. Questions traitées
Questions Q8.1 à Q8.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q8.1** - Pourquoi ne pas commencer une transformation DevOps en installant tous les outils ?

Parce que les outils ne règlent pas les problèmes d'organisation. Chez NovaTech, la plus grosse attente (36 h) vient de la validation par lots, et aucun outil ne la supprimera si la règle reste la même. Installer plein d'outils d'un coup, c'est aussi beaucoup de coûts et de formation, des équipes qui ne savent pas pourquoi elles les utilisent, et le risque d'automatiser un mauvais processus.

Mieux vaut d'abord comprendre où ça bloque, changer les façons de travailler, puis choisir les outils qui aident vraiment. DORA conseille de découper la transformation en petites étapes et de mesurer avant d'agir.

Source : https://dora.dev/guides/how-to-transform/

- **Q8.2** - Qui sont les parties prenantes de la transformation chez NovaTech, et quelles sont leurs attentes ?

| Partie prenante | Attente principale |
|---|---|
| **Direction** | Savoir d'où vient le problème, avec des preuves et un plan réaliste |
| **Responsable métier** | Des évolutions livrées à temps pour les campagnes, et de la visibilité |
| **Développeurs** | Moins d'attente entre la fin du code et la mise en production |
| **Exploitation (Ops)** | Être prévenue à temps, et avoir un retour arrière testé |
| **Sécurité** | Des contrôles plus tôt, et savoir qui valide les exceptions |
| **Clients** | Un site et un paiement qui fonctionnent |

Ces attentes viennent des témoignages du dossier (`01_Contexte_et_temoignages.md`).

- **Q8.3** - Quels critères retiendriez-vous pour choisir un projet pilote ?

- **Assez important pour être visible :** il doit montrer un vrai gain, sinon personne n'y croira.
- **Pas trop risqué :** si ça rate, ça ne doit pas toucher les clients. Pour NovaTech, on éviterait de commencer par le module de paiement.
- **Court :** des résultats visibles en quelques semaines.
- **Une équipe volontaire :** c'est plus facile avec des gens motivés qu'avec une équipe forcée.
- **Mesurable :** on doit pouvoir comparer avant et après, par exemple le lead time ou l'attente de validation.

- **Q8.4** - Comment prioriser les actions selon leur valeur, leur effort et leur risque ? Appliquez la méthode à trois actions.

On note chaque action de 1 (faible) à 3 (fort) sur la valeur, l'effort et le risque, puis on commence par celles qui apportent beaucoup pour peu d'effort et peu de risque.

| Action | Valeur | Effort | Risque | Priorité |
|---|:---:|:---:|:---:|---|
| Validation quotidienne des petits changements | 3 | 1 | 1 | **1** : gros gain sur les 36 h d'attente, presque rien à installer |
| Revue sans blâme après chaque incident | 2 | 1 | 1 | **2** : facile, mais l'effet se voit sur le long terme |
| Retour arrière automatisé du module de paiement | 3 | 3 | 2 | **3** : très utile, mais demande du temps et touche une partie sensible |

C'est une estimation de l'équipe, pas un calcul précis : les notes sont à discuter avec NovaTech.

- **Q8.5** - Quels risques et quelles résistances anticipez-vous, et comment les traiter ?

- **« On a toujours fait comme ça » :** surtout côté validation. On répond par un essai court et réversible plutôt qu'en imposant le changement.
- **La peur de perdre le contrôle :** l'Ops et la sécurité peuvent craindre plus d'incidents. On garde le comité pour les changements à risque, et on suit le taux d'échec pendant l'essai.
- **Le manque de temps :** les équipes sont prises par le travail courant. Il faut réserver du temps pour l'amélioration, sinon elle passe toujours après.
- **L'essoufflement :** si les résultats tardent, l'élan retombe. Il faut montrer des petites réussites rapidement.

Source : https://www.kotterinc.com/methodology/8-steps/

- **Q8.6** - Au bout de 30 jours, comment décider de poursuivre, d'ajuster ou d'arrêter un pilote ?

On fixe les critères avant de commencer, pour ne pas décider « au feeling » :

- **Poursuivre :** l'indicateur visé s'est amélioré (par exemple, l'attente de validation passe sous 12 h) et le taux d'échec n'a pas augmenté.
- **Ajuster :** il y a un progrès, mais pas assez, ou un problème à corriger. On modifie une chose et on refait un essai.
- **Arrêter :** rien ne s'améliore, ou le pilote a causé un incident sérieux.

La décision se prend avec l'équipe concernée, en regardant les chiffres et en écoutant ce que les gens ont vécu.

- **Q8.7** - Construisez une feuille de route 30/60/90 jours cohérente avec vos expérimentations, avec indicateurs et critères d'arrêt.

| Période | Actions | Indicateur | Critère d'arrêt |
|---|---|---|---|
| **30 jours** | Validation quotidienne des changements à faible risque (pilote). Revue sans blâme après chaque incident. Tests automatiques et recherche de secrets sur chaque PR. | Attente avant validation (36 h aujourd'hui) | Un incident causé par un changement validé de cette façon |
| **60 jours** | Changements à faible risque pré-approuvés, comité réservé au paiement. Environnement de test décrit en Docker Compose. Notification d'échec de la CI envoyée dans un canal d'équipe. | Lead time médian (55 h aujourd'hui) | Hausse du change fail rate (15 % aujourd'hui) |
| **90 jours** | Retour arrière testé et feature flag sur le module de paiement. Tableau de bord DORA revu chaque mois avec la direction. | Temps de restauration (100 min en moyenne aujourd'hui) | Pas d'amélioration après deux revues mensuelles |

Lien avec nos expérimentations : les tests et la CI (TP 4), Docker Compose (TP 5) et la notification ChatOps ont été testés en local. Le reste (validation quotidienne, feature flag, tableau de bord) n'a pas été testé, ce sont des propositions.

- **Q8.8** - Comment adapter la gouvernance ITSM et la sécurité à l'échelle de l'organisation sans freiner les équipes ?

En adaptant le niveau de contrôle au niveau de risque. Les changements simples passent par la revue d'un collègue et la CI, sans attendre un comité. Le comité ne garde que les changements sensibles, comme le paiement.

Pour la sécurité, l'idée est de mettre les contrôles directement dans le pipeline (recherche de secrets, analyse du code) plutôt qu'en fin de parcours. Les équipes ont un retour rapide, et la sécurité n'a plus à tout relire à la main. Il faut aussi écrire clairement qui valide les exceptions de sécurité, puisque c'est flou aujourd'hui.

Source : https://dora.dev/capabilities/streamlining-change-approval/

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Diagnostic, parties prenantes, conduite du changement

- **Le diagnostic :** avant de changer quoi que ce soit, comprendre où sont les vrais problèmes, en séparant les faits des hypothèses.
- **Les parties prenantes :** toutes les personnes concernées par le changement. Elles n'ont pas les mêmes attentes, et il faut les écouter toutes.
- **Le projet pilote :** tester le changement en petit, sur une équipe et pendant peu de temps, avant de le généraliser.
- **La conduite du changement :** aider les gens à changer leurs habitudes, avec des explications, des petites réussites visibles et du temps, plutôt qu'en imposant.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [How to transform](https://dora.dev/guides/how-to-transform/) | DORA (Google Cloud) | 22/10/2026 | Découper la transformation en petites étapes livrées progressivement, mesurer l'état de départ, donner aux équipes des problèmes à résoudre plutôt que des tâches, et réserver du temps à l'amélioration. Une transformation imposée d'en haut comme un projet ponctuel mène au désengagement. | Guide de référence, publié par Google. Mis à jour le 06/10/2025. |
| [The 8 Steps for Leading Change](https://www.kotterinc.com/methodology/8-steps/) | John Kotter, Kotter International | 22/10/2026 | Les 8 étapes du changement, dont créer un sentiment d'urgence, lever les obstacles et générer des victoires à court terme, à communiquer tôt et souvent. | Site d'un cabinet de conseil qui vend sa méthode. Pas de date. |
| [ING's agile transformation](https://karriere.mckinsey.de/ings-agile-transformation) | McKinsey (entretien avec Peter Jacobs et Bart Schlatmann, ING) | 22/10/2026 | En 2015, ING Netherlands réorganise les 3 500 personnes de son siège en environ 350 équipes de 9. Lancement de 5 ou 6 équipes pilotes. La culture est présentée comme l'élément le plus important. | Entretien publié par un cabinet de conseil, avec des dirigeants qui parlent de leur propre réussite. Publié le 10/01/2017. |
| [Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/) | DORA (Google Cloud) | 22/10/2026 | Remplacer l'approbation lourde par la revue entre pairs et les tests automatisés, et garder un contrôle renforcé pour les changements à haut risque. | Basé sur les enquêtes DORA. Mis à jour le 30/10/2025. |

## 4. Exemple professionnel commenté

En 2015, la banque néerlandaise ING a réorganisé les 3 500 personnes de son siège en petites équipes pluridisciplinaires de 9 personnes, en mélangeant marketing, produit et développement IT. Avant de basculer tout le monde, elle a lancé 5 ou 6 équipes pilotes pour ajuster le modèle. Les dirigeants expliquent que le plus dur n'a pas été l'organisation, mais la culture : ils ont même perdu des personnes compétentes dont l'état d'esprit ne correspondait pas.

Commentaire : Ce qui nous frappe, c'est que même une grande banque, avec des régulateurs inquiets au départ, a commencé par des pilotes avant de généraliser. Les dirigeants préviennent aussi qu'adopter seulement une partie du modèle en gardant l'ancienne structure crée de la frustration. Pour NovaTech, la leçon est la même : commencer petit, mais aller au bout de ce qu'on teste. Il faut quand même garder en tête que c'est un entretien où les dirigeants parlent de leur propre réussite.

## 5. Expérimentation / analyse
**Piste :** Feuille de route et comité de direction fictif

- Hypothèse : Une feuille de route qui commence par des actions simples, peu risquées et mesurables a plus de chances d'être acceptée par la direction de NovaTech qu'un grand plan qui change tout d'un coup.

- Protocole / méthode : On a résumé l'état initial de NovaTech à partir des modules précédents, priorisé les actions selon leur valeur, leur effort et leur risque (Q8.4), puis réparti ces actions sur 30, 60 et 90 jours (Q8.7). Chaque action est reliée à une expérimentation réalisée ou signalée comme non testée. La feuille de route doit ensuite être présentée à un comité de direction fictif, joué par l'équipe.

- Résultat observé ou simulation :

  **État initial de NovaTech**

  | Dimension | Constat |
  |---|---|
  | Culture | Équipes en silo, l'Ops découvre les changements la veille, réunion de crise sans retour d'expérience après l'incident |
  | Processus | 110 h de délai dont 80 % d'attente, 36 h pour la seule validation |
  | Outils | Pas de retour arrière testé, pas d'environnement de test partagé |
  | Sécurité | Contrôles trop tardifs, personne de désigné pour valider les exceptions |
  | Contraintes | Pas de budget cloud, effectifs et budget inconnus |

  **Ce qui a été testé et ce qui ne l'a pas été**

  | Action de la feuille de route | Testée ? | Preuve |
  |---|---|---|
  | Tests automatiques et CI | Oui, en local et sur GitHub | TP 4 : run rouge puis vert |
  | Recherche de secrets dans la CI | Oui, résultat à confirmer sur le run | Test avec une fausse clé (branche `J2_testing`) |
  | Environnement en Docker Compose | Oui, en local | TP 5 : `preuves/tp5-docker.md` |
  | Notification ChatOps dans un canal | Oui, vers Discord, résultat à confirmer | Branche `J2_testing_nicolas` |
  | Validation quotidienne, revue sans blâme, feature flag, tableau de bord DORA | Non | Propositions seulement |

- Ce que ce résultat ne prouve pas : La feuille de route n'a pas été mise en œuvre, donc ses effets sont attendus, pas mesurés. Nos tests techniques ont été faits sur une petite application d'exercice, pas sur le vrai système de NovaTech. Les notes de priorité sont une estimation de l'équipe. Enfin, sans connaître le budget et les effectifs de NovaTech, on ne peut pas affirmer que le plan est réalisable dans ces délais.

## 6. Application à NovaTech
- Problème visé : La direction veut « des preuves, des options et un plan réaliste », mais ne sait pas par où commencer.

- Action envisagée : Lancer un pilote de 30 jours sur la validation quotidienne des changements à faible risque, avec une équipe volontaire, en dehors du module de paiement. À la fin, un point de décision avec la direction : poursuivre, ajuster ou arrêter, selon les critères fixés au départ (Q8.6).

- Indicateur et risque :

    - Indicateurs : l'attente avant validation (36 h aujourd'hui, objectif sous 12 h) et le change fail rate (15 %), pour vérifier qu'aller plus vite ne casse rien.

    - Risques : que le pilote soit jugé trop tôt, avant d'avoir assez de données. Que l'équipe pilote reprenne ses anciennes habitudes une fois l'essai terminé. Ou que la direction veuille tout généraliser trop vite après un premier bon résultat.

## 7. Preuves déposées
**Attendu :** Plan 30/60/90 avec responsables, risques et métriques
- Liens commits / MR / CI / fichiers :
  - Feuille de route 30/60/90 : Q8.7 de ce fichier (à reporter dans `novatech/feuille-de-route.md`) ;
  - Priorisation des actions : Q8.4 de ce fichier ;
  - Expérimentations sur lesquelles s'appuie le plan : TP 4 (branche `J2_testing`), TP 5 (`preuves/tp5-docker.md`), ChatOps (branche `J2_testing_nicolas`) ;
  - Slides 9 et 10 de la soutenance : à rédiger.

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a aidé à rédiger les réponses Q8.1 à Q8.8 et les sections 2 à 7, et a vérifié chaque source (auteur, date, ce que dit réellement la page). Les priorités et la feuille de route sont à relire et valider par l'équipe.

## 10. Questions ouvertes / blocages

- Quels sont le budget et les effectifs réels de NovaTech ? Sans eux, les délais de la feuille de route restent une hypothèse.
- Le comité de direction fictif reste à jouer en équipe avant la soutenance.
