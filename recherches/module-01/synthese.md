# Module 01 - Introduction, origine, Business/IT

**Équipe : GroupeHuitre** …  **Contributeurs : Nicolas.P, Romain, Adam, Morgan** …  **Date :20/10/2026**

## 1. Questions traitées
Questions Q1.1 à Q1.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q1.1** - Comment définiriez-vous DevOps en une phrase, sans citer aucun outil ? 

Le DevOps est l’agrégation de plusieurs principes culturels et d'outils améliorant la capacité d'une organisation à livrer des applications tout en gardant ou améliorant la qualité et la fiabilité de celles-ci via l’automatisation permettant une intégration et livraison continue. 

- **Q1.2** - D’où vient le terme « DevOps » et quels événements des années 2008-2009 ont marqué l’émergence du mouvement ?

Ce terme est apparu en octobre 2009, lors du premier DevOpsDays à Gand, en Belgique organisé par Patrick Debois. Cependant il y a eu des précurseurs comme :  

Andrew Clay Shafer et Patrick Debois se rencontrent en 2008 à la conférence Agile et discutent d’infrastructure Agile ;

John Allspaw et Paul Hammond présentent en 2008 “10+ Deploys Per Day : Dev and Ops Cooperation at Flickr”, c’était une révélation pour l’industrie.

- **Q1.3** - D’après les témoignages de **01_Contexte_et_temoignages.md**, quels objectifs des équipes Dev, Ops, sécurité et métier de NovaTech sont contradictoires ?

Le métier veut de la visibilité et de la rapidité pour ses campagnes commerciales, le développeur constate que validations et déploiements prennent plus de temps que le développement lui-même, l'exploitante découvre des changements la veille de la mise en production sans rollback testé (elle privilégie la stabilité), la sécurité veut des contrôles plus tôt et une responsabilité claire des exceptions. 

Ce qui est contradictoire va donc être que les développeurs trouvent le temps de validation et de déploiement trop long alors que la sécurité trouve qu’il y a un manque d’informations sur ces validations, ce qui implique qu’en plus de prendre du temps le travail n’est pas clair ce qui est un fonctionnement anormal.

- **Q1.4** - Pourquoi DevOps n’est-il ni un intitulé de poste, ni une équipe dédiée, ni une chaîne d’outils ? Donnez un exemple d’entreprise où cette confusion a posé un problème.

L'incident se déroule à une époque où le mot "DevOps" émergeait à peine, il reste le cas d'école universellement cité pour illustrer l'échec d'une approche purement "outils et processus manuels" sans culture de collaboration ni automatisation globale, nous parlons de l'entreprise Knight Capital (firme de courtage financier). Cette dernière traitait le déploiement comme une tâche purement technique et manuelle confiée à des techniciens isolés. 

En août 2012, lors du déploiement d'un nouveau logiciel sur ses serveurs, un technicien a oublié de copier manuellement le code sur le huitième serveur de l'entreprise. Ce serveur contenait un ancien code obsolète, mais qui partageait le même code d'activation que la nouvelle fonctionnalité. 

Lors de l'ouverture des marchés, ce serveur a réactivé l'ancienne fonction défectueuse et s'est mis à acheter et vendre des millions d'actions à perte de manière frénétique. L'équipe technique, fonctionnant en silo et sans outils de surveillance partagés avec les développeurs, a mis 45 minutes à comprendre le problème. 

Pour tenter de le résoudre, ils ont supprimé le nouveau code des autres serveurs, aggravant encore la situation. 

En conséquence, en a peine une heure, Knight Capital a perdu 440 millions de dollars, ce qui a conduit à la faillite de l'entreprise et à son rachat en urgence. 

- **Q1.5** - Quelles conséquences métier (clients, chiffre d’affaires, image) l’incident du 16 octobre peut-il avoir, et quelles informations manquent pour les évaluer ?

Voici les conséquences possibles liées à l'incident du 16 octobre. 

Conséquences clients : 

- Paiements impossibles ou en erreur, qui peuvent emmener à des paniers / commandes abandonnées ; 

- Des paiements en double, ou débités sans commande validée (demande de remboursement) ; 

- Génération de tickets et d’appels envers le support ; 

- Perte de confiance des clients. 

Chiffre d'affaires : 

- Des ventes perdues pendant 95 minutes, un vendredi en fin d’après-midi, un créneau fort pour un site de commerce en ligne ; 

- Des coûts liés au remboursement, gestes commerciaux, etc. 

- Possibles litiges juridiques causés par le non-traitement, ou le traitement de commandes erronées. 

Image : 

- Des avis négatifs ou des messages publics sur les réseaux sociaux ;  

- Une atteinte à la crédibilité sur un point sensible qu’est le paiement, où la confiance est essentielle ; 

- Des risques possibles si des données de paiement ont été touchées ;

- Perte de confiance sur les marchés (si entreprise cotée). 

Plusieurs éléments manquent pour évaluer réellement l'impact de l'incident. 

Premièrement, nous ne savons pas combien de clients ont été touchés, combiens de transactions ont échouées pendant les 95 minutes. Dans un second temps on ne connait pas le CA habituel normalement enregistré sur ce créneau horaire, ni les modalités concernant les remboursements. 
Enfin nous n’avons pas connaissance si le service de paiement a été impacté ou complètement indisponible.

- **Q1.6** - Parmi les causes possibles des difficultés de NovaTech, lesquelles relèvent des outils, des processus ou de la collaboration ? Sur quels faits du dossier vous appuyez-vous ?

| Problématique                                        | Outils | Processus | Collaboration | Dossier                    |
|------------------------------------------------------|:------:|:---------:|:-------------:|----------------------------|
| Goulot d'étranglement (attente)                      |        |     X     |       X       | 02Processus_actuel         |
| Pas de recensement des problèmes de chaque équipe    |        |           |       X       | 01_Contexte_et_temoignages |
| Plusieurs jours entre le dernier commit et le déploiement |   X    |     X     |               | 04_Deploiements_fictifs    |

- **Q1.7** - Le stéréotype « Dev veut changer, Ops veut stabiliser » est-il encore pertinent avec le cloud, le SRE et le Platform Engineering ? Argumentez avec au moins deux sources.

 Aujourd'hui, l'objectif n'est plus d'opposer le changement à la stabilité, mais de gérer mathématiquement le risque de changement et d'industrialiser le libre-service. 
 
 Avec le Cloud, l'infrastructure est devenue du logiciel. Les développeurs peuvent provisionner des ressources via du code, tandis que les opérationnels codent les règles de sécurité et de scalabilité. La frontière physique ayant disparu, le conflit historique lié au matériel n'a plus lieu d'être, Le Site Reliability Engineering (SRE), initié par Google, a résolu structurellement la tension entre changement et stabilité grâce à la notion de budget d'erreur. 
 
 Tant que le budget d'erreur est respecté (bonne fiabilité), les développeurs ont le feu vert pour déployer de nouvelles fonctionnalités à un rythme soutenu, dès lors que le budget est consommé (mauvaise fiabilité), la priorité absolue de toute l'équipe bascule temporairement sur la fiabilisation du système. 
 
 On peut également citer le passage au modèle de responsabilité partagée via le Cloud permettant d’externaliser certaines problématiques de stockage hardware, sécurité du datacenter, gestion des accès, abstraction avec des services plus ou moins managé par le fournisseur cloud, le reste toutefois présent. Le provider Cloud devient donc un acteur décisif au même titre que le Dev et Ops.

 Sources :

 https://www.bytebase.com/blog/dev-sre-ops-devops-difference/
 https://www.stephane-robert.info/docs/devops/fondamentaux/sre/

 - **Q1.8** - Comment démontreriez-vous à la direction de NovaTech la valeur d’une démarche DevOps sans inventer de retour sur investissement ?

 La démarche DevOps permettrait d’avoir des gains sur plusieurs points, le premier étant de réduire le time to market puisque cette démarche a pour but d’automatiser les déploiements. Cette automatisation permettra de déployer plus régulièrement, si possible de manière journalière, cette rapidité de déploiement aura un impact positif sur le temps de debug post deploiement. 
 
 Tout ce gain de temps est donc un gain de production et économique. L’ajout de tests automatisés, d’un environnement de test et de monitoring permettrait de mieux prévenir les incidents lors du déploiement et protéger davantage la disponibilité du service de paiement, et donc réduire les pertes de l’entreprise liée à ces incidents de déploiement et rollbacks échéants. 

## 2. Concepts expliqués avec nos mots

Le DevOps est l’agrégation de plusieurs principes culturels et d'outils améliorant la capacité d'une organisation à livrer des applications tout en gardant ou améliorant la qualité et la fiabilité de celles-ci via l’automatisation permettant une intégration et livraison continue.

## 3. Sources consultées et vérifiées

| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [Culture DevOps](https://www.stephane-robert.info/docs/devops/fondamentaux/culture-devops/) | Stéphane Robert (blog technique personnel) | 21/10/2026 | Le cloisonnement Dev/Ops crée des objectifs contradictoires (livrer vite / éviter les incidents). Les déploiements difficiles poussent à regrouper les changements, ce qui rend chaque livraison plus risquée et plus lente. | Source individuelle, non académique. Les chiffres « organisations traditionnelles » (2 à 6 mois de délai, 30 à 60 % d'échec) ne sont pas sourcés sur la page. Mise à jour le 01/10/2026, sans date de publication initiale. |
| [SEC – Press Release 2013-222](https://www.sec.gov/newsroom/press-releases/2013-222) | U.S. Securities and Exchange Commission (SEC) | 21/10/2026 | Le 1er août 2012, un déploiement erroné de code sur le routeur d'ordres de Knight Capital a provoqué plus de 460 M$ de pertes en 45 minutes. 97 alertes automatiques envoyées avant l'ouverture n'ont pas été traitées. Amende : 12 M$. | Source officielle et primaire, la plus fiable du lot. Elle ne donne pas le détail technique (nombre de serveurs, flag réutilisé). |
| [Case Study 4: The $440 Million Software Error at Knight Capital](https://www.henricodolfing.ch/case-study-4-the-440-million-software-error-at-knight-capital/) | Henrico Dolfing (consultant indépendant) | 21/10/2026 | Lors du déploiement, l'un des 8 serveurs n'a pas reçu le nouveau code. Un flag réutilisé y a réactivé l'ancienne fonction « Power Peg », qui a envoyé plus de 4 millions d'ordres. | Source secondaire qui s'appuie surtout sur l'ordonnance de la SEC. Le titre parle de 440 M$, mais la SEC retient plus de 460 M$. Le texte ne dit pas que le déploiement était manuel. Publié le 05/06/2019. |
| [Dev vs SRE vs Ops vs DevOps](https://www.bytebase.com/blog/dev-sre-ops-devops-difference/) | Tianzhou, Bytebase (éditeur de logiciels) | 21/10/2026 | Distinction des rôles : Dev écrit le code, Ops gère l'infrastructure, SRE est une évolution des Ops avec des compétences de développement (SLO/SLI/SLA), et DevOps est un mode de fonctionnement où les développeurs prennent en charge les tâches Ops. | Blog commercial qui fait la promotion de ses produits. La prédiction sur l'avenir des rôles est une opinion non étayée. Publié le 15/07/2022. |
| [SRE – Site Reliability Engineering](https://www.stephane-robert.info/docs/devops/fondamentaux/sre/) | Stéphane Robert (blog technique personnel) | 21/10/2026 | Le SRE est né chez Google en 2003 (Benjamin Treynor Sloss). Avec un SLO de 99,9 %, le budget d'erreur est d'environ 43 min d'indisponibilité par mois, et les déploiements sont gelés quand ce budget est épuisé. Le SRE est une implémentation concrète du DevOps. | Source individuelle. Pour l'origine du SRE, mieux vaut citer en plus la source primaire, le livre *Site Reliability Engineering* de Google (sre.google). Mise à jour le 13/10/2026. |

## 4. Exemple professionnel commenté

L'incident se déroule à une époque où le mot "DevOps" émergeait à peine, il reste le cas d'école universellement cité pour illustrer l'échec d'une approche purement "outils et processus manuels" sans culture de collaboration ni automatisation globale, nous parlons de l'entreprise Knight Capital (firme de courtage financier). Cette dernière traitait le déploiement comme une tâche purement technique et manuelle confiée à des techniciens isolés. 

En août 2012, lors du déploiement d'un nouveau logiciel sur ses serveurs, un technicien a oublié de copier manuellement le code sur le huitième serveur de l'entreprise. Ce serveur contenait un ancien code obsolète, mais qui partageait le même code d'activation que la nouvelle fonctionnalité. 

Lors de l'ouverture des marchés, ce serveur a réactivé l'ancienne fonction défectueuse et s'est mis à acheter et vendre des millions d'actions à perte de manière frénétique. L'équipe technique, fonctionnant en silo et sans outils de surveillance partagés avec les développeurs, a mis 45 minutes à comprendre le problème. 

Pour tenter de le résoudre, ils ont supprimé le nouveau code des autres serveurs, aggravant encore la situation. 

En conséquence, en a peine une heure, Knight Capital a perdu 440 millions de dollars, ce qui a conduit à la faillite de l'entreprise et à son rachat en urgence.

Commentaire : Ce qui frappe dans cette histoire, c’est que l’erreur de départ est presque banale : un serveur oublié sur huit. Le vrai problème, c’est que tout reposait sur une manip à la main, sans vérification, et que les alertes envoyées avant l’ouverture n’ont été lues par personne. C’est exactement ce que le DevOps cherche à éviter : avec un déploiement automatisé et une équipe qui communique, cet oubli n’aurait sans doute jamais coûté aussi cher.

## 5. Expérimentation / analyse
**Piste :** Conflit de priorités Dev/Ops/métier, incident NovaTech

- Hypothèse : L'incident du 16 octobre vient moins d'un problème technique que d'un manque de coordination entre les équipes. Chaque équipe poursuit son propre objectif (le métier veut livrer à temps pour les campagnes, le Dev veut livrer son code, l'Ops veut éviter les incidents, la sécurité veut valider), personne n'a de vision commune du déploiement.

- Protocole / méthode : On a repris les témoignages (`01_Contexte_et_temoignages.md`) et la chronologie de l'incident (`03_Incident_fictif.md`), puis on a rejoué la réunion d'après-incident en se répartissant les rôles (métier, Dev, Ops, la sécurité à tour de rôle). On a ensuite noté les frictions et classé chaque élément en fait du dossier ou en hypothèse. On a aussi regardé la ligne D17 du fichier `04_Deploiements_fictifs.csv`, qui correspond à l'incident.

- Résultat observé ou simulation :

  - Le déploiement a eu lieu un vendredi à 16h45, en fin de semaine.
  - Le code était prêt depuis le 13/10 à 8h45, soit environ 80 h (3 jours et 8 h) d'attente avant la mise en production.
  - Le retour arrière n'était pas accessible tout de suite : à 17h05, Dev et Ops se réunissent dans l'urgence.
  - Le service a été rétabli au bout de 95 minutes.
  - L'Ops dit découvrir certaines modifications « la veille », et la sécurité ne sait pas toujours qui valide quoi. Chacun travaille de son côté et les passages de relais se font au dernier moment.
  - Sur 30 jours, 3 déploiements sur 20 ont provoqué un incident, donc le 16/10 n'est pas un cas isolé.
  - Pendant le jeu de rôle, chacun avait tendance à défendre son équipe plutôt qu'à chercher une solution commune.

- Ce que ce résultat ne prouve pas : On ne connaît pas la cause réelle de l'incident : il nous manque les logs, les métriques, les résultats des tests et le détail des actions de restauration. Le manque de collaboration reste donc une hypothèse cohérente avec les témoignages, pas une cause démontrée. Le jeu de rôle repose sur des témoignages simulés et sur notre interprétation, il ne remplace pas de vrais entretiens. Enfin, rien ne prouve que plus de collaboration aurait évité l'incident, ni qu'on peut chiffrer son coût pour l'entreprise.

## 6. Application à NovaTech
- Problème visé : Les équipes travaillent chacune de leur côté et se passent le relais au dernier moment. L'Ops découvre les modifications la veille de la mise en prod, la sécurité valide trop tard, et le jour de l'incident la procédure de retour arrière n'était pas prête.

- Action envisagée : Faire participer l'Ops et la sécurité dès la préparation d'un changement, pas juste au moment du déploiement.

- Indicateur et risque :

    - Indicateurs : la part des changements connus de l'Ops au moins 2 jours avant le déploiement (à mesurer, on n'a pas la valeur actuelle), le change fail rate (3/20 = 15 % sur la période) et le temps de restauration (95 min pour l'incident du 16/10).

    - Risques : le point hebdo peut devenir une réunion de plus, qui ajoute de l'attente au lieu d'en retirer. Les équipes peuvent aussi le vivre comme un contrôle et pas comme de la collaboration. Et comme les données sont fictives et l'échantillon petit, une baisse des incidents ne prouverait pas à elle seule que l'action marche.

## 7. Preuves déposées
**Attendu :** Diagnostic : symptôme / hypothèse / information manquante / effet métier
- Liens commits / MR / CI / fichiers :

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

RAS

## 10. Questions ouvertes / blocages

RAS
