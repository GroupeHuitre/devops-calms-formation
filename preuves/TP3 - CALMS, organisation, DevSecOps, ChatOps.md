# TP3 - CALMS, organisation, DevSecOps, ChatOps

**Objectif du TP (`consignes/06_TP_et_experimentations.md`) :** appliquer CALMS à NovaTech, organiser le travail de l'équipe, vivre une revue d'incident sans blâme, concevoir et tester une notification ChatOps, et comprendre deux contrôles DevSecOps « shift left » déjà présents dans la CI.

## 1. Matrice CALMS
**Fichier :** `novatech/analyse-calms.md`.
Les cinq dimensions (Culture, Automation, Lean, Measurement, Sharing) sont chacune reliées à un fait ou une hypothèse du dossier NovaTech, une action, un responsable provisoire et une mesure de suivi. Exemple marquant : la dimension *Sharing* relie le cloisonnement Dev/Ops/Sécurité/métier observé dans l'incident du 16/10 à la notification ChatOps désormais réelle (voir point 3). Une section dédiée relie les cinq dimensions au framework Three Ways (Flow / Feedback / Continual Learning).

## 2. Revue d'incident sans blâme
**Fichier :** `experiences/retour-incident.md`.
Reconstruction de la chronologie factuelle de l'incident du 16/10/2026 (déploiement 16h45 → erreurs signalées 16h52 → réunion improvisée 17h05 → rétablissement 18h20), suivie d'un scénario de réunion rejoué (dialogue Métier/Dev/Ops/Sécurité) et d'actions avec propriétaire provisoire.
**Statut honnête :** faute de temps, le scénario a été écrit à l'avance à partir des positions réelles de chaque fonction dans le dossier NovaTech, plutôt que joué en direct par les 4 membres. Ce n'est pas le compte-rendu d'une réunion qui a eu lieu.

## 3. ChatOps - conçu puis réellement testé
**Fichiers :** `experiences/chatops.md`, `.github/workflows/ci.yml`, `preuves/discord_webhook.png`.

- **Conception (TP3) :** schéma du message en Mermaid dans `experiences/chatops.md`, événement (échec CI) → notification → canal → action humaine attendue. Critères retenus : notification uniquement sur échec (pas sur succès, pour éviter le bruit), information minimale et non sensible (branche, commit, lien de run), URL du webhook stockée en secret GitHub (`DISCORD_WEBHOOK_URL`), jamais en clair.
- **Réalisation (dépasse la simulation prévue par la CI fournie) :** un vrai webhook Discord a été créé et branché sur le job `tests` de `ci.yml`. **Preuve réelle, non simulée :** le 21 octobre 2026 à 14h47, le bot `ChatOpsBot` a posté dans le salon `#chat-ops` du serveur Discord du groupe un message d'échec CI précis, avec la branche `J2_testing_nicolas`, le commit `1f5bed1bbece71645a1710544acd30cb3c1566f6` et le lien direct vers le run GitHub Actions (`.../actions/runs/39602448029`). Capture : `preuves/discord_webhook.png`.

## 4. DevSecOps « shift left »
**Fichier :** section dédiée dans `novatech/analyse-calms.md`.
- Le job `secrets` (`gitleaks`) détecte des secrets au format reconnaissable déjà commités dans Git ; il ne couvre pas les dépendances vulnérables, les droits du pipeline lui-même, ni un secret diffusé ailleurs qu'en Git.
- Le `Dockerfile` de `application/` applique un utilisateur non root et un `HEALTHCHECK`, ce dernier répond directement à une faiblesse de l'incident du 16/10 (détection par signalement client plutôt que par une alerte automatique).

## Tableau récapitulatif des preuves

| Date | Preuve (fichier ou URL) | Commit / run | Réel, simulé ou bloqué | Commentaire |
|---|---|---|---|---|
| 2026-10-21 | `preuves/discord_webhook.png` | `1f5bed1bbece71645a1710544acd30cb3c1566f6` / [run 39602448029](https://github.com/GroupeHuitre/devops-calms-formation/actions/runs/39602448029) | **Réel** | Notification ChatOps Discord déclenchée par un échec CI réel, pas une simulation |
| 2026-10-20/21 | `novatech/analyse-calms.md` | - | Analyse documentaire | Matrice CALMS construite à partir du dossier NovaTech, pas d'observation d'une organisation réelle |
| 2026-10-20/21 | `experiences/retour-incident.md` | - | **Simulé** | Scénario de réunion écrit à l'avance, pas joué en direct par les 4 membres (manque de temps) |

## Limites à documenter
- La revue d'incident reste une préparation écrite, pas une session vécue par l'équipe.
- La matrice CALMS s'appuie sur un dossier fictif ; les causes identifiées sont des hypothèses, pas des preuves.
- Le ChatOps réel ne couvre que les échecs du job `tests` de la CI, pas un vrai incident de production (pas de monitoring applicatif branché).
- Gitleaks et les choix du `Dockerfile` réduisent des risques connus sans garantir l'absence de vulnérabilité.

## Prochaine action #TODO
Organiser la session réelle de revue d'incident (15-20 min, les 4 membres), compléter `experiences/retour-incident.md` avec ce qui aura été réellement décidé, et mettre à jour ce résumé en conséquence.
