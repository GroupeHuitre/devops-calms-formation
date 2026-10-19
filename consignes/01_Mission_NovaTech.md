# Mission NovaTech

## Votre mission

Vous êtes trois consultants DevOps juniors missionnés pour aider **NovaTech**, entreprise *entièrement fictive* de commerce en ligne. Une évolution du module de paiement déployée à 16 h 45 a déclenché des erreurs ; le service a été rétabli à 18 h 20 (95 minutes entre ces deux repères). Les livraisons sont jugées lentes, les contrôles manuels nombreux et les échanges Dev/Ops difficiles. 
**Question du comité de direction :** « Comment améliorer la livraison de valeur, la collaboration, la sécurité et la fiabilité de NovaTech, en montrant ce que vous pouvez réellement expérimenter en 3 jours et en proposant une feuille de route réaliste pour la suite ? »

Vous devez comprendre DevOps sous ses dimensions **Business, organisationnelle, culturelle et technique**, et expliquer comment une entreprise pourrait engager l'adoption. On n'attend ni cloud de production ni infrastructure payante.

## Conditions de travail

- **Groupes de 3** ; responsabilité tournante chaque jour : coordination, recherche/validation documentaire, expérimentation et preuves. Toutes les personnes participent à chacune des activités.
- **Un assistant IA** par équipe ou des échanges transparents consignés dans le repository. L'IA est autorisée ; les sources primaires et les résultats techniques doivent être vérifiés.
- **Un repository GitHub/GitLab par groupe**, privé sauf instruction contraire de l'établissement, donnant accès au formateur. Toutes les huit recherches sont versionnées dans `recherches/module-XX/synthese.md`.
- **Issues / tableau Kanban** : visualiser les travaux (À faire, En cours, En revue, Terminé). Définir une politique simple de revue et, si utile, une limite WIP.
- **Pull requests / merge requests** : faire relire au moins une contribution de chaque membre ; l'historique montre les décisions, pas seulement un dépôt final.
- Ne pas publier de secrets, identifiants personnels, données réelles ou informations confidentielles dans le dépôt ni dans un assistant IA non approuvé.

## Dossier client disponible

- `donnees-novatech/01_Contexte_et_temoignages.md` : entretiens fictifs avec métier, Dev, Ops, sécurité.
- `donnees-novatech/02_Processus_actuel.csv` : étapes et durées fictives de livraison.
- `donnees-novatech/03_Incident_fictif.md` : récit et lacunes de preuve de l'incident.
- `donnees-novatech/04_Deploiements_fictifs.csv` : 20 déploiements simulés, pour l'atelier DORA.
- `application/` : petit service Python déjà fonctionnel, utilisé pour Git, tests, CI et environnement local.

**Attention :** les données du dossier ne prouvent pas toutes les causes. Vos conclusions doivent distinguer **faits fournis / hypothèses / informations à demander / actions proposées**.

## Mission jour par jour

Le contenu de chaque module, les questions de recherche (Q1.1 à Q8.8) et les consignes d'expérimentation sont dans `consignes/02_Programme_recherches_8_modules.md`.

**Jour 1 - comprendre :** rechercher les modules 1–3 ; diagnostiquer NovaTech, appliquer les Three Ways et comparer Agile/Lean/ITSM ; ouvrir et organiser le dépôt ; présenter vos apprentissages et blocages.

**Jour 2 - expérimenter :** rechercher les modules 4–6 ; CALMS, organisation, sécurité, ChatOps et Kanban ; collaborative Git ; mettre en place / exécuter les tests et une CI ; explorer une configuration As Code ; montrer preuves et limites.

**Jour 3 - proposer :** rechercher les modules 7–8 ; calculer/interpréter les indicateurs DORA fictifs ; concevoir une action PDCA et feuille de route 30/60/90 jours ; présenter **exactement 10 slides** devant la classe avec démonstration et questions individuelles.

## Livrables non négociables

1. Huit synthèses de modules avec sources et application à NovaTech.
2. Une fiche pour chaque concept structurant : Three Ways, CALMS, Kanban, DevSecOps, ChatOps, Git/CI/CD, IaC et DORA (regroupement possible si justifié).
3. Diagnostic, VSM, matrice CALMS, analyse des métriques, feuille de route.
4. Dépôt Git collaboratif, expérience de tests/CI (échec + correction observables ou blocage reproductible), fichier As Code, réflexion de sécurité.
5. Bilans fin J1 et J2, journal de décisions, suivi Kanban et bilan J3.
6. Présentation finale **10 slides exactement** et démonstration.

## Liberté et responsabilité

Vous pouvez choisir vos sources, méthodes, outils compatibles et priorités complémentaires. Vous n'êtes pas obligés de présenter la même solution que les autres groupes. Vous devez néanmoins maîtriser les concepts obligatoires des 8 modules. Un concept compris mais non testé doit être identifié comme tel ; un test exécuté sans compréhension ne vaut pas preuve de maîtrise.

## Éthique des preuves

- Preuve technique : lien vers commit, résultat de commande, run CI, capture annotée ou observation datée.
- Distinguez « pipeline » de « livraison continue » et de « déploiement continu ».
- Signalez ce que vous n'avez pas pu vérifier.
