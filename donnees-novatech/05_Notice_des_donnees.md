# Notice des données NovaTech

## `02_Processus_actuel.csv`

Chaque ligne comporte : temps actif, temps d'attente et hypothèse de cause qui **n'a pas été prouvée**. Sommes : temps actif = 22 h ; attente = 88 h ; délai cumulé = 110 h ; part d'attente = 88 / 110 = 80 %. Ces valeurs servent à une première cartographie VSM simplifiée, sans modéliser les parallélismes et écarts de calendrier d'une vraie organisation.

## `04_Deploiements_fictifs.csv`

Vingt événements de déploiement du 20 septembre au 19 octobre 2026 inclus, période pédagogique de **30 jours calendaires**. `committed_at` est le commit représentatif retenu pour l'exercice ; `deployed_at` le déploiement du changement associé. `incident_change=1` indique une modification ayant causé une dégradation nécessitant une intervention ; `unplanned_deployment_rework=1` indique un déploiement non planifié lié à la résolution d'un incident ; `failed_deployment_recovery_min` est fourni uniquement pour les trois changements échoués.

**Limites :** dans une organisation réelle, un déploiement peut contenir plusieurs commits, le périmètre de succès doit être défini et les événements de rework doivent être identifiés par une convention métier. Ce jeu synthétique simplifie ces questions. Le temps de restauration DORA actuel est celui d'un déploiement ayant échoué, pas le temps de récupération de toute panne, quelle qu'en soit la cause.

## Attendus d'analyse

Présenter les **cinq mesures du modèle DORA actuel** : fréquence, change lead time, failed deployment recovery time, change fail rate, deployment rework rate. Montrer le numérateur, le dénominateur, les unités, la période et les limites. Ne pas conclure que des seuils fixes reflètent automatiquement une bonne ou une mauvaise organisation.
