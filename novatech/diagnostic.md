# Diagnostic de NovaTech

Consolidé à partir de l'analyse réelle de l'équipe : `recherches/module-01/synthese.md` (jeu de rôle, cas Knight Capital), `recherches/module-02/synthese.md` (données de processus) et `docs/bottleneck_analysis.md` (goulots par domaine).

| Symptôme établi | Hypothèse de cause | Preuve manquante | Effet Business / IT | Priorité proposée |
|---|---|---|---|---|
| Incident du 16/10 : le code était prêt dès le 13/10 à 8h45, déployé seulement le 16/10 à 16h45 (≈ 80 h d'attente), puis 95 min d'indisponibilité du paiement | Validation par lots + retour arrière non immédiatement accessible (`03_Incident_fictif.md`) | Logs applicatifs, résultat des tests avant déploiement, identifiant exact du changement | Ventes perdues sur un vendredi fin d'après-midi (créneau fort e-commerce), remboursements et litiges possibles, image | Haute |
| 3 déploiements sur 20 (15 %) ont provoqué un incident sur les 30 jours observés (D04, D11, D17 dans `04_Deploiements_fictifs.csv`) | Processus de validation/tests insuffisant pour détecter les changements à risque avant mise en prod | Détail des causes de chaque incident, résultats de tests associés à D04 et D11 | Le 16/10 n'est pas un cas isolé : risque récurrent sur le service de paiement | Haute |
| Ops découvre certaines modifications la veille de la mise en prod ; la sécurité ne sait pas toujours qui valide les exceptions (`01_Contexte_et_temoignages.md`) | Absence de visibilité partagée Dev/Ops/Sécurité sur le calendrier des changements | Fréquence réelle des découvertes tardives, processus actuel de communication | Risque accru d'incidents, charge et stress pour Ops, exceptions de sécurité non tracées | Haute |
| 80 % du délai de livraison est de l'attente, pas du travail actif (88 h / 110 h, `novatech/value-stream-map.md`) | Validation par lots (36 h) et environnement de test non partagé (24 h) concentrent la majorité de l'attente | Capacité réelle (débit) des équipes de validation et de test | Livraisons jugées « trop lentes » pour les campagnes commerciales (témoignage métier) | Haute |
| Pas de recensement centralisé des problèmes remontés par chaque équipe (`recherches/module-01/synthese.md`, Q1.6) | Absence d'outil ou de process de suivi partagé entre équipes (Kanban, RACI) | Outils de suivi actuellement utilisés en interne par chaque équipe, s'il y en a | Décisions prises sans vision d'ensemble, priorisation difficile | Moyenne |

## Parties prenantes, risques, sécurité

- **Parties prenantes :** métier (chiffre d'affaires, campagnes commerciales), développement (vélocité, qualité), exploitation (stabilité, astreinte), sécurité (conformité, exceptions), direction (décision, budget). Les clients finaux ne sont représentés qu'indirectement (témoignages), ce qui est une limite du dossier.
- **Risques :** le paiement concentre un risque financier direct et répété (3 incidents sur 20 déploiements, pas un cas isolé) ; l'absence de rollback testé allonge le temps de restauration en cas de récidive ; la validation par lots agrège des changements plus gros donc plus risqués.
- **Sécurité :** contrôles arrivant tard dans le cycle, responsabilité des exceptions non tracée par écrit.

## Ce que nous refusons de conclure sans données

- Que l'incident du 16/10 a une cause unique et connue : il manque les logs, les métriques, les résultats de tests et le détail des actions de restauration (`recherches/module-01/synthese.md`). Le manque de collaboration reste une hypothèse cohérente avec les témoignages, pas une cause démontrée.
- Que l'étape « Validation changement » (36 h d'attente) est *la* contrainte du système au sens de la théorie des contraintes : on sait seulement que c'est la plus longue attente, pas que c'est un vrai goulot de capacité (`recherches/module-02/synthese.md`, Q2.5).
- Que plus de collaboration aurait empêché l'incident, ou que son coût pour l'entreprise est chiffrable avec les données actuelles.
- Que les gains simulés dans la boucle PDCA (voir `novatech/value-stream-map.md`) se produiraient réellement : ce sont des objectifs fixés par l'équipe, pas des mesures observées.
