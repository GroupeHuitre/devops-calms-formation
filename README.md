# Découvrir et mettre en place Devops 

## Dépôt d'apprentissage du groupe XX

**Équipe (prenoms des 3 personnes) :** … 

## Démarrage : créer le dépôt de votre groupe 

Une seule personne du groupe crée le dépôt, puis invite les deux autres membres **et le formateur**. Le dépôt doit être **privé**.

**Option A — GitHub (recommandée)**

1. Sur la page du dépôt modèle, cliquer sur **Use this template** → **Create a new repository**.
2. Nom : `novatech-groupe-XX` (XX = numéro de votre groupe, de 01 à 08). Visibilité : **Private**.
3. **Settings → Collaborators → Add people** : ajouter les deux autres membres et le formateur `franklin-tutorials`.
4. Chaque membre clone le dépôt du groupe : `git clone <URL du dépôt du groupe>`.
5. Vérifier l'onglet **Actions** : le workflow « CI NovaTech » doit être vert après le premier push.

**Option B — GitLab**

1. Créer un projet vide : **New project → Create blank project**, nom `novatech-groupe-XX`, visibilité **Private**, sans README.
2. Copier le modèle dans ce projet :
   ```bash
   git clone <URL du dépôt modèle> novatech-groupe-XX
   cd novatech-groupe-XX
   git remote set-url origin <URL du projet du groupe>
   git push -u origin main
   ```
3. **Manage → Members → Invite members** : ajouter les deux autres membres et le formateur `ftutorials` avec le rôle **Maintainer** (ou **Reporter** pour le formateur).
4. Vérifier **Build → Pipelines**. Sur gitlab.com, l'utilisation des runners partagés peut exiger une vérification du compte ; en cas de blocage, appliquer le plan B du TP4.

Ensuite : compléter l'en-tête de ce README (équipe, formateur, plateforme), créer une Issue par module et le tableau Kanban.

## Mission

Découvrir DevOps par la recherche, l'expérimentation et une proposition de transformation **Business, culturelle, organisationnelle et technique** de la société NovaTech (cas fictif). Les consignes complètes sont dans `consignes/` : commencer par `consignes/01_Mission_NovaTech.md`, puis `consignes/02_Programme_recherches_8_modules.md` (notions, questions et expérimentations de chaque module).

## Navigation

- `consignes/` : mission (`01`), programme de recherche des 8 modules avec questions et consignes d'expérimentation (`02`), déroulé des 3 jours (`03`), règles IA (`04`), soutenance (`05`), TP (`06`).
- `donnees-novatech/` : dossier client fictif (entretiens, processus, incident, déploiements).
- `recherches/module-01/` à `module-08/` : **8 synthèses obligatoires** avec sources vérifiées, exemples, analyses, expérience et application.
- `notions/` : fiches Three Ways, CALMS, DORA, DevSecOps, ChatOps, Kanban, CI/CD, IaC et autres.
- `novatech/` : diagnostic, VSM, CALMS, indicateurs DORA, feuille de route.
- `application/` : exemple de service et tests ; code réellement expérimenté.
- `infrastructure/` : descriptions versionnées et limites.
- `experiences/` et `preuves/` : hypothèses, captures, logs, URLs et résultats.
- `suivi/` : bilans des trois journées.
- `presentation/soutenance-10-slides.md` : **10 slides maximum**.
- `sources.md` : Citer les sources pour aller plus loin.
- `.github/workflows/ci.yml` (GitHub) et `.gitlab-ci.yml` (GitLab) : CI fournie (tests, recherche de secrets, notification ChatOps simulée).

## Suivi de projet

- Tableau Kanban (lien) : …
- Issues (lien) : …
- Politique de revue et définition de « terminé » : …
- Répartition des responsabilités et rotation : …
