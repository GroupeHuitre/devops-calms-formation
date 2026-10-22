# Value Stream Map simplifiée

Source : `donnees-novatech/02_Processus_actuel.csv`. Goulots détaillés par domaine (gouvernance, process, qualité, infra) : `docs/bottleneck_analysis.md`. Simulation d'amélioration complète : `recherches/module-02/synthese.md` (section 5).

| Étape | Actif (h) | Attente (h) | Question à poser |
|---|---:|---:|---|
| Spécification | 2 | 6 | Le backlog est-il priorisé et cadré (Definition of Done) avant que le développement démarre ? |
| Développement | 12 | 4 | Le découpage en commits atomiques réduirait-il l'attente de revue qui suit ? |
| Revue de code | 2 | 10 | Un template de PR et des tests automatisés obligatoires réduiraient-ils le temps d'attente de relecture ? |
| Tests | 3 | 24 | L'environnement de test est-il partagé et standardisé (ex. Docker) entre les équipes ? |
| Validation changement | 1 | 36 | La validation se fait-elle par lots, ou pourrait-elle être découpée en changements plus petits et plus fréquents ? |
| Déploiement | 2 | 8 | La fenêtre de déploiement restreinte est-elle une contrainte technique, ou une habitude que l'automatisation (CI/CD, IaC) pourrait lever ? |

Temps actif total = 22 h ; attente totale = 88 h ; délai cumulé = 110 h ; proportion de temps d'attente = 88 / 110 = **80 %**.

## Goulet probable / incertitudes

La plus longue attente est **« Validation changement »** (36 h), suivie de **« Tests »** (24 h), loin devant le temps actif de développement (12 h). Ça pointe vers un goulot de gouvernance/validation plutôt que de développement.

**Incertitude à ne pas gommer :** on ne connaît ni la capacité réelle ni le débit de l'étape de validation (nombre de changements traitables par semaine, taux d'occupation). Une attente longue peut aussi être une habitude de calendrier (comité périodique) plutôt qu'une vraie saturation de ressource. On ne peut donc pas affirmer que cette étape est **la** contrainte au sens de la théorie des contraintes avec les seules données du CSV (cf. `recherches/module-02/synthese.md`, Q2.5).

## Hypothèse d'amélioration et Three Ways associés

L'équipe a simulé trois actions d'amélioration en ne changeant qu'une seule variable à la fois (méthode PDCA, détail complet en `recherches/module-02/synthese.md`). **Les valeurs « après » sont des objectifs fixés par l'équipe, pas des mesures réelles.**

| Action simulée | Attente gagnée | Délai total | Part d'attente |
|---|---:|---:|---:|
| Aucune (situation actuelle) | 0 h | 110 h | 80 % |
| A — Validation quotidienne au lieu de par lots (36 h → 12 h) | 24 h | 86 h | 74 % |
| B — Environnement de test partagé (24 h → 8 h) | 16 h | 94 h | 77 % |
| C — Reviewers désignés chaque jour (10 h → 4 h) | 6 h | 104 h | 79 % |
| A + B + C combinées | 46 h | 64 h | 66 % |

- **Flow :** l'action A (validation quotidienne) est celle qui ferait gagner le plus de temps, cohérent avec le goulot identifié sur « Validation changement ».
- **Feedback :** l'action B (environnement de test partagé) accélère le retour sur les tests, donc la détection des régressions.
- **Continual Learning & Experimentation :** la démarche elle-même (tester une seule variable à la fois, mesurer, ajuster) incarne cette troisième voie — c'est la boucle PDCA proposée en Q2.7.

**Limite assumée par l'équipe :** même en combinant les trois actions, l'attente reste majoritaire (66 %) — il reste donc de la marge sur d'autres étapes. Le modèle additionne simplement des durées : il ne tient pas compte du travail en parallèle, de la variabilité de charge, ni de la capacité réelle des équipes. Rien ne garantit non plus qu'une validation plus rapide n'augmenterait pas le taux d'incident.
