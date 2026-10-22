# Module 03 - Agile, Lean, ITSM/ITIL

**Équipe :** GroupeHuitre  **Contributeurs :** Nicolas.P, Romain, Adam, Morgan  **Date :** 21/10/2026

## 1. Questions traitées
Questions Q3.1 à Q3.8 de `consignes/02_Programme_recherches_8_modules.md` (indiquer le numéro de chaque question traitée, et vos propres questions éventuelles).

- **Q3.1** - Quelles sont les quatre valeurs du Manifeste agile ?

Le Manifeste agile (2001) définit quatre valeurs :

- Les individus et leurs interactions plus que les processus et les outils.
- Des logiciels opérationnels plus qu'une documentation exhaustive.
- La collaboration avec les clients plus que la négociation contractuelle.
- L'adaptation au changement plus que le suivi d'un plan.

Le manifeste précise que les éléments de droite gardent de la valeur, mais que ceux de gauche sont prioritaires.

Source :

https://agilemanifesto.org/iso/fr/manifesto.html

- **Q3.2** - Qu'est-ce que l'ITSM, et à quoi sert ITIL ?

L'ITSM (IT Service Management), c'est la façon dont une entreprise organise ses services informatiques de bout en bout : les planifier, les mettre en place, les gérer et les améliorer, pour qu'ils répondent aux besoins des utilisateurs et de l'entreprise. Ce n'est pas un logiciel en particulier, plutôt une approche.

La gestion de connaissances en est une bonne pratique : l'équipe informatique crée de la documentation tout en résolvant des problèmes. C'est susceptible de réduire considérablement la charge de travail du centre de services en offrant aux clients internes et externes des options en libre-service.

ITIL est le référentiel de bonnes pratiques le plus utilisé pour mettre en place l'ITSM. Il ne s'agit pas d'un outil ni d'une norme obligatoire, mais d'un guide qui décrit comment organiser ces services (la norme certifiable, c'est plutôt ISO/IEC 20000). Sa version ITIL 4, publiée en 2019, propose 34 pratiques (gestion des incidents, gestion des changements, etc.) et ses principes reprennent des idées d'Agile, Lean et DevOps.

Exemple chez NovaTech : la « validation changement » qui fait attendre les modifications 36 h correspond à une pratique ITSM de gestion des changements.

Sources :

https://www.ibm.com/think/topics/it-service-management
https://www.grcsolutions.io/itil

- **Q3.3** - Scrum garantit-il à lui seul des mises en production fiables ? Pourquoi ?

Non. Scrum aide à organiser le travail de l'équipe (sprints, rôles, réunions), mais il ne dit pas comment tester, déployer ou surveiller un logiciel en production. Il ne fait pas non plus travailler ensemble les développeurs et l'exploitation.

Par exemple, chez NovaTech : les développeurs testent leur code, mais l'exploitation découvre les changements la veille de la mise en production, sans retour arrière prêt. Résultat : l'incident du 16 octobre.

Tout dépend de l’application également de l’application des règles du Scrum book, en effet le fait de faire des équipes interdisciplinaires (composée de dev, qa, devops, ops, po) permettrais de sensibiliser les acteurs aux besoins et problématiques des autres, et d’organiser le travail selon les besoins business en priorité.

Paradoxalement, la course au sprint pour répondre à des délais peut aussi dégrader la qualité et la fiabilité de la mise en production. Il y’a donc également un delta entre le Scrum guide tel que décrit, et son application selon les entreprises qui peut être largement interprétée.

Pour des mises en production fiables, il faut ajouter des pratiques DevOps : tests automatiques, CI/CD, retour arrière prêt et surveillance de la production.

Source :

https://scrumguides.org/scrum-guide.html

- **Q3.4** - Quels gaspillages au sens du Lean repérez-vous dans le processus de NovaTech ?

En Lean, un gaspillage est tout ce qui prend du temps sans apporter de valeur au client. Chez NovaTech, on en trouve plusieurs :

1. Les attentes : le travail attend 80 % du temps (88 h sur 110 h).
2. Le travail bloqué : des changements terminés attendent d'être validés ensemble, par lots. La validation dépend d’individus clés et bloque la chaine de livraison de valeur.
3. Les passages de relais : l'exploitation découvre les changements la veille de la mise en production, il n’y a pas de logs, tests ou monitoring.
4. Les défauts : l'incident du 16 octobre a demandé une réparation, puis un correctif le lendemain, les changements ne sont pas testés en amont, et le rollback est long et couteux.
5. Le temps perdu à chercher : la procédure de retour arrière n'était pas accessible pendant l'incident. Il n’y a pas de post mortem en cas d’incident pour le résoudre plus rapidement en cas de nouvelle occurence.

- **Q3.5** - Comment concilier une gestion des changements de type ITIL (validations, comité de changement) avec des livraisons petites et fréquentes ?

On peut garder un contrôle sur les changements sans tout ralentir, en adaptant la validation au niveau de risque :

- Les petits changements à faible risque sont pré-approuvés : ITIL appelle ça des « changements standard ». Ils n'ont pas besoin de passer en comité.
- La validation se fait par la relecture d'un collègue (pull request), enregistrée dans l'outil, au lieu d'attendre une réunion.
- Les tests automatiques et la CI vérifient chaque changement avant la mise en production.
- La validation d’un déploiement en environnement de test avant l’application de ces changements en production ajouterait un filet de sécurité supplémentaire.
- Du monitoring et logs permettrait de controller davantage la qualité pour accélérer les validations.
- Le comité de changement ne garde que les changements à haut risque, comme le module de paiement de NovaTech.

Chez NovaTech, ça permettrait de réduire les 36 h d'attente avant validation, tout en gardant un contrôle sur les changements sensibles.

Source :

https://dora.dev/capabilities/streamlining-change-approval/

- **Q3.6** - Que traite le Lean que les outils de CI ne résolvent pas ?

La CI automatise une seule partie du travail : construire et tester le code. Le Lean, lui, regarde tout le chemin, de la demande du client jusqu'à la livraison, et cherche à supprimer ce qui ne sert à rien, la vision est beaucoup plus holistique, orientée sur l’humain, l’équipe et les outils.

Le Lean traite donc des problèmes que la CI ne voit pas :

- les attentes en dehors du code : priorisation, validation, fenêtres de mise en production ;
- les règles d'organisation, comme la validation par lots ;
- les passages de relais entre les équipes ;
- l'amélioration continue : mesurer, tester un changement, apprendre.

Exemple chez NovaTech : une CI plus développé pourrait réduire l'attente des tests (24 h), mais elle ne changerait rien à l'attente de la validation (36 h) ni à celle de la spécification (6 h). Sur 88 h d'attente, la majorité ne dépend pas d'un outil, mais de l'organisation.

- **Q3.7** - Proposez une organisation de NovaTech combinant Agile, Lean, ITSM et DevOps : qui décide de quoi, avec quels risques ?

Proposition d'organisation pour NovaTech :

- Le responsable métier (rôle de Product Owner, Agile) décide des priorités : quoi livrer et dans quel ordre.
- Une équipe produit commune, avec Dev, Ops et sécurité (DevSecOps), décide comment construire, tester et déployer. Les changements à faible risque sont validés par la relecture d'un collègue.
- La sécurité définit les contrôles automatiques du pipeline et décide des exceptions.
- Le comité de changement (ITSM) ne valide que les changements à haut risque, comme le module de paiement, et pilote la gestion des incidents.
- Les changements sont déployés sur un environnement de Staging, et le succès ou l’échec de ces déploiements conditionne le déploiement en Production.
- La direction fixe les objectifs et, avec l'équipe, revoit chaque mois les attentes et les indicateurs pour choisir la prochaine amélioration (Lean).

Risques :

- Le Product Owner peut être débordé par les demandes ;
- L'équipe peut manquer de compétences en exploitation ou en sécurité au début, le temps d’accumuler un historique de logs ;
- Les contrôles automatiques ne détectent pas tout ;
- Le comité de changement peut revenir à ses anciennes habitudes et tout ralentir ;
- Les équipes peuvent résister au changement ;
- Les effectifs et le budget de NovaTech ne sont pas connus : cette organisation reste une hypothèse.

Source :

https://dora.dev/capabilities/streamlining-change-approval/

- **Q3.8** - ITIL 4 et DevOps : convergence ou concurrence ? Comparez au moins deux sources et précisez leurs dates.

Au départ, on pensait que les deux s’opposaient. Avec ITIL v3, chaque changement devait passer devant un comité de validation, le CAB, et forcément ça ralentit tout. Alors que le DevOps, c’est justement l’inverse : livrer souvent, par petits bouts.

En fait, ITIL a pas mal évolué avec sa version 4, sortie en 2019. D’après un article d’EasyVista (29/06/2021), le CAB n’est plus obligatoire pour chaque changement. Une validation par un collègue peut suffire, et certains changements courants n’ont même plus besoin d’être validés. On y retrouve aussi des idées qui viennent directement du DevOps, comme l’intégration continue ou le feedback.

Atlassian (12/05/2020) raconte un peu la même chose avec sa propre expérience : ils ont arrêté de tout faire valider par un comité et laissent plus d’autonomie aux équipes. Et d’après eux, ça ne pose pas de problème pour respecter les règles de conformité, tant que l’automatisation permet de garder une trace de tout.

DORA (Google Cloud, mis à jour le 30/10/2025) est plus tranché. Leurs études montrent qu’un comité de validation ralentit les livraisons, et qu’en plus il ne réduit pas vraiment les erreurs. Ils conseillent plutôt de faire relire le code par un collègue et de miser sur les tests automatiques.

Du coup, pour nous, ce n’est pas vraiment une concurrence. ITIL 4 sert à bien gérer les services, et le DevOps à livrer vite sans prendre trop de risques, les deux peuvent très bien aller ensemble. Le problème, c’est surtout quand une entreprise reste sur un ITIL « à l’ancienne », avec un comité pour tout. C’est un peu ce qu’on voit chez NovaTech, où la validation par lots fait attendre les changements 36 h.

Sources :

https://www.easyvista.com/blog/the-change-enablement-practice-what-changed-with-change-in-itil-4-easyvista
https://www.atlassian.com/engineering/best-practices-for-change-management-in-the-age-of-devops
https://dora.dev/capabilities/streamlining-change-approval/

## 2. Concepts expliqués avec nos mots
**Point incontournable :** Complémentarités et rôles des différentes approches

Chaque approche répond à une question différente, c'est pour ça qu'elles se complètent plus qu'elles ne s'opposent :

- **Agile :** quoi livrer et dans quel ordre ? On travaille par petites étapes avec le client et on s'adapte au changement.
- **Lean :** où est-ce qu'on perd du temps ? On regarde tout le chemin de la demande à la livraison et on enlève ce qui n'apporte rien au client.
- **ITSM / ITIL :** comment on fait tourner le service ? Gestion des incidents, des changements, des niveaux de service.
- **DevOps :** comment on livre vite sans tout casser ? Collaboration Dev/Ops, automatisation, feedback.

Les tensions apparaissent surtout quand une approche est appliquée « à l'ancienne », par exemple un comité de changement qui valide tout alors qu'on veut livrer souvent.

## 3. Sources consultées et vérifiées
| URL / document | Auteur ou institution | Consulté le | Affirmation vérifiée | Réserve |
|---|---|---|---|---|
| [Manifeste pour le développement Agile de logiciels](https://agilemanifesto.org/iso/fr/manifesto.html) | Kent Beck, Martin Fowler, Ken Schwaber, Jeff Sutherland et 13 autres signataires | 21/10/2026 | Les quatre valeurs, et la phrase « Nous reconnaissons la valeur des seconds éléments, mais privilégions les premiers ». | Source primaire, texte officiel en français. Publié en 2001. |
| [The Scrum Guide](https://scrumguides.org/scrum-guide.html) | Ken Schwaber et Jeff Sutherland | 21/10/2026 | Les équipes Scrum sont pluridisciplinaires (10 personnes ou moins) et chaque Increment doit respecter la Definition of Done. Le guide ne décrit aucune pratique de test, de déploiement ou d'exploitation. | Source primaire. Version de novembre 2020. Le guide dit que l'équipe est responsable de l'« operation » du produit, sans dire comment. |
| [What is IT service management (ITSM)?](https://www.ibm.com/think/topics/it-service-management) | IBM | 21/10/2026 | L'ITSM consiste à planifier, mettre en place, gérer et optimiser la livraison des services IT de bout en bout. ITIL est le cadre le plus adopté pour le mettre en œuvre, et ITIL 4 date de 2019. La gestion des connaissances, avec une base en libre-service, en est un outil central. ITSM et DevOps sont souvent vus comme complémentaires. | Page d'un éditeur qui vend des outils ITSM. Ni auteur ni date de publication. |
| [What is ITIL?](https://www.grcsolutions.io/itil) | GRC Solutions | 21/10/2026 | ITIL 4 compte 34 pratiques (14 de management général, 17 de management des services, 3 de management technique). Ses 7 principes directeurs reflètent ceux d'Agile, DevOps et Lean. ITIL est un guide de bonnes pratiques, pas une norme : la norme certifiable est ISO/IEC 20000. | Entreprise privée de conformité qui vend des formations ITIL. Ne donne pas l'année de sortie d'ITIL 4. Publié le 26/11/2025. |
| [PeopleCert gets ready to share the future of ITIL 4 at Pink23](https://www.peoplecert.org/news-and-announcements/2023/pc-pink23) | PeopleCert (propriétaire d'ITIL) | 21/10/2026 | ITIL 4 a été lancé en 2019. PeopleCert présente une session sur les liens entre DevOps, Lean, Agile et ITIL 4. | Page d'annonce d'événement, peu détaillée. Non datée, mais l'événement a eu lieu en février 2023. |
| [The Change Enablement Practice: What Changed with Change in ITIL 4](https://www.easyvista.com/blog/the-change-enablement-practice-what-changed-with-change-in-itil-4-easyvista) | EasyVista (Stephen Mann, ITSM.tools) | 21/10/2026 | Dans ITIL 4, le « change management » devient « change enablement », réécrit pour tenir compte du DevOps. Le CAB n'est plus obligatoire pour chaque changement (délégation, changements standards, revue entre pairs). | Blog d'un éditeur de logiciels ITSM. L'auteur n'est pas clairement indiqué comme signataire. Ce n'est pas le texte officiel d'ITIL. Publié le 29/06/2021. |
| [Best practices for change management in the age of DevOps](https://www.atlassian.com/engineering/best-practices-for-change-management-in-the-age-of-devops) | Isabel Nyo, Atlassian | 21/10/2026 | Atlassian a remplacé l'approbation par CAB par l'autonomie des équipes. Les principes DevOps peuvent fonctionner avec la conformité si l'automatisation garantit la traçabilité. | Retour d'expérience d'une seule entreprise, qui vend aussi des outils ITSM. Ne parle pas d'ITIL 4. Publié le 12/05/2020. |
| [Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/) | DORA (Google Cloud) | 21/10/2026 | Une approbation externe lourde (CAB) ralentit la livraison, et rien ne prouve qu'elle réduise le taux d'échec des changements. Il vaut mieux la revue par les pairs et les tests automatisés. Le CAB garde un rôle de coordination. | Basé sur les données d'enquête de DORA, pas sur une expérience contrôlée. Ne cite pas ITIL. Mis à jour le 30/10/2025. |

## 4. Exemple professionnel commenté

Atlassian, l'éditeur de Jira, avait comme beaucoup d'entreprises un comité qui devait approuver les changements avant leur mise en production. Le problème, c'est que certaines demandes pouvaient attendre des mois. En 2020, l'entreprise explique avoir remplacé ce fonctionnement par plus d'autonomie pour les équipes : une revue quotidienne des mises en production où l'on pose des questions au lieu de donner un feu vert, et de l'automatisation pour garder une trace de chaque changement. Aujourd'hui, Atlassian déploie plusieurs fois par jour, tout en restant soumise à des règles de conformité comme SOX.

Commentaire : Ce qu'on retient, c'est qu'ils n'ont pas supprimé le contrôle, ils l'ont déplacé. Au lieu d'un comité qui valide tout à la fin, le contrôle se fait au fil de l'eau, par les équipes et par les outils. C'est exactement la convergence ITIL / DevOps dont on parle en Q3.8. Il faut quand même garder en tête que c'est Atlassian qui raconte sa propre réussite, et qu'ils vendent justement des outils pour faire ça.

## 5. Expérimentation / analyse
**Piste :** Cas : quels apports pour 4 problèmes NovaTech ?

- Hypothèse : Aucune approche ne règle à elle seule les problèmes de NovaTech. Agile, Lean, ITSM et DevOps apportent chacun une partie de la réponse, et leur combinaison couvre mieux les difficultés qu'une seule approche.

- Protocole / méthode : On a choisi quatre difficultés issues de notre diagnostic (module 1) et de notre VSM (module 2). Pour chacune, on a noté ce que chaque approche peut apporter, en s'appuyant sur un fait du dossier ou une source, puis le risque principal. On a ensuite cherché une tension entre deux approches et un compromis.

- Résultat observé ou simulation :

  **Matrice problème / approche / justification / risque**

  | Problème NovaTech (fait du dossier) | Approche | Apport possible | Justification | Risque |
  |---|---|---|---|---|
  | **P1 - Validation par lots : 36 h d'attente pour 1 h de travail** (`02_Processus_actuel.csv`) | Agile | Livrer de plus petits changements, plus souvent | Manifeste agile : logiciel opérationnel et adaptation au changement | Des sprints trop courts sous pression de délai |
  | | Lean | Repérer et réduire l'attente (gaspillage) | 80 % du délai total est de l'attente (Q2.3) | Réduire l'attente sans regarder la qualité |
  | | ITSM | Changements standards pré-approuvés, CAB réservé au haut risque | ITIL 4 change enablement (EasyVista, 2021) | Le CAB reprend ses habitudes et valide tout |
  | | DevOps | Revue par les pairs et tests automatiques à la place du comité | DORA (2025) : pas de preuve que le CAB réduise les échecs | Des tests automatiques incomplets donnent une fausse confiance |
  | **P2 - L'Ops découvre les changements la veille** (témoignage de l'exploitante) | Agile | Équipe pluridisciplinaire, Ops présente dès la planification | Scrum Guide : équipes pluridisciplinaires | L'Ops est sollicitée par trop d'équipes à la fois |
  | | Lean | Réduire les passages de relais | Le passage de relais est un gaspillage (Q3.4) | Rester sur le papier si personne ne change sa façon de travailler |
  | | ITSM | Calendrier des changements partagé | Gestion des changements ITIL | Un outil de plus que personne ne consulte |
  | | DevOps | Tableau Kanban commun et notifications de la CI | Culture de collaboration Dev/Ops | Trop de notifications, plus personne ne les lit |
  | **P3 - Incident du 16/10 : retour arrière inaccessible, 95 min de restauration** (`03_Incident_fictif.md`) | Agile | Rétrospective après l'incident | Amélioration régulière de l'équipe | La rétro tourne à la recherche de coupable |
  | | Lean | Post mortem et amélioration continue (PDCA) | Apprendre de chaque défaut | Des actions décidées mais jamais suivies |
  | | ITSM | Gestion des incidents et des problèmes, procédure de retour arrière documentée | Pratiques ITIL de gestion des incidents | Une procédure écrite mais jamais testée |
  | | DevOps | Retour arrière automatisé et testé dans le pipeline, monitoring | Feedback rapide (Three Ways) | Coût et temps de mise en place |
  | **P4 - Le métier manque de visibilité sur les livraisons** (témoignage du responsable métier) | Agile | Product Owner, backlog priorisé, démonstrations régulières | Manifeste agile : collaboration avec le client | Le PO est débordé par les demandes |
  | | Lean | Rendre le flux visible de bout en bout (VSM) | VSM du module 2 | Une cartographie faite une fois et jamais mise à jour |
  | | ITSM | Niveaux de service et communication des changements prévus | Gestion des niveaux de service ITIL | Des engagements de service trop rigides |
  | | DevOps | Indicateurs DORA partagés avec le métier | Fréquence de déploiement, lead time | Des chiffres mal interprétés par le métier |

  **Tension identifiée :** l'ITSM « classique » veut contrôler chaque changement avec un comité, alors que DevOps veut des changements petits et fréquents. Si on garde le comité pour tout, les livraisons fréquentes vont juste rallonger la file d'attente.

  **Compromis proposé :** adapter le contrôle au risque. Les changements à faible risque passent par la revue d'un collègue et les tests automatiques, et le comité ne garde que les changements à haut risque, comme le module de paiement (voir Q3.5).

- Ce que ce résultat ne prouve pas : C'est une analyse sur papier, faite à partir d'un dossier fictif et de quelques sources, sans observer une vraie organisation. La matrice montre que les approches peuvent se compléter, pas que leur combinaison marcherait chez NovaTech. Les risques sont nos suppositions, et on n'a pas de données pour savoir lequel est le plus probable. Enfin, l'étape de relecture de la matrice par un autre membre reste à faire.

## 6. Application à NovaTech
- Problème visé : Le comité de validation traite tous les changements de la même façon, ce qui crée 36 h d'attente, alors que la plupart des changements ne présentent pas de risque particulier.

- Action envisagée : Classer les changements par niveau de risque. Les changements à faible risque deviennent des « changements standards » validés par la revue d'un collègue et la CI, et le comité ne garde que les changements à haut risque (module de paiement, sécurité).

- Indicateur et risque :

    - Indicateurs : l'attente avant validation (36 h aujourd'hui), la part des changements qui passent encore en comité, et le change fail rate (3/20 = 15 % sur la période) pour vérifier que la qualité ne baisse pas.

    - Risques : mal classer un changement risqué en « faible risque », et le laisser passer sans contrôle suffisant. Le comité peut aussi avoir du mal à lâcher le contrôle et continuer à tout vouloir valider.

## 7. Preuves déposées
**Attendu :** Matrice problème/approche/justification
- Liens commits / MR / CI / fichiers :
  - Matrice dans la section 5 de ce fichier ;
  - Relecture de la matrice par un autre membre : à faire.

## 8. Contribution et maîtrise des trois membres
- Personne A : Researcher (Romain)
- Personne B : Product Owner (Morgan)
- Personne C : Dev (Nicolas.P)
- Personne D : Dev (Adam)

## 9. Apport de l'IA et vérification

L'IA a été utilisée pour mettre en forme le fichier, vérifier les sources citées (auteur, date, ce que dit réellement la page), aider à reformuler la Q3.8 et rédiger un premier jet des sections 2, 4, 5 et 6. Les deux sources d'origine de la Q3.2 n'ont pas pu être vérifiées (lien cassé, page illisible) : elles ont été remplacées par des pages IBM et GRC Solutions, et la définition de l'ITSM a été précisée à partir de la page IBM.

## 10. Questions ouvertes / blocages

- Les sources de la Q3.2 viennent d'entreprises privées : on n'a pas pu consulter le texte officiel d'ITIL 4, qui est payant.
- PeopleCert annonce maintenant une nouvelle version d'ITIL (« ITIL Version 5 ») : faut-il en tenir compte dans notre réponse sur ITIL 4 ?
