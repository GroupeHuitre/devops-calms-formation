# Incident de production - NovaTech

Un **vendredi 16 octobre 2026**, une évolution du module de paiement est mise en production à **16h45**. Des erreurs utilisateurs sont signalées peu après. Le service est rétabli à **18h20** ; cet intervalle correspond à **95 minutes**. Il ne faut pas assimiler le temps de restauration à un temps de détection, ni présumer de la cause racine.

## Chronologie connue 

- 16h45 : nouveau déploiement.
- 16h52 : premières erreurs signalées.
- 17h05 : réunion improvisée Dev/Ops ; procédure de retour arrière non immédiatement accessible.
- 18h20 : service rétabli.

## Pièces manquantes

Logs applicatifs et d'accès, métriques de production, identifiant du changement, alertes, statut du monitoring, versions exactes, résultat des tests avant déploiement, détail des actions de restauration, impact financier et nombre de clients touchés.

## Questions à traiter

1. Quels sont les faits observés et les hypothèses ?
2. Quelles informations demander avant une analyse de cause racine ?
3. Quelles actions humaines, organisationnelles et techniques pourraient réduire le risque futur ?
4. Quel feedback mettre en place pour détecter plus tôt une régression ?
5. Comment organiser un retour d'expérience sans recherche de coupables ?
